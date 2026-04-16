import xbmc
import xbmcplugin
import xbmcgui
import sys
import requests

handle = int(sys.argv[1])

DROPBOX = "https://dl.dropbox.com/scl/fi/nln0qvhqwt6fx0b57zoy2/sportLive.txt?rlkey=qpodxt2auc0wyy46o9qdmto3b&st=8ixfgfxq"

def pegar_canais():
    try:
        texto = requests.get(DROPBOX, timeout=10).text
        linhas = [l.strip() for l in texto.split("\n") if l.strip()]
        canais = []

        for linha in linhas:
            if "|" in linha:
                nome, link = linha.split("|")
            else:
                nome = "Canal ao vivo"
                link = linha

            canais.append((nome, link))

        return canais
    except:
        return []

def listar():
    canais = pegar_canais()

    if not canais:
        xbmcgui.Dialog().notification("Erro", "Lista vazia", xbmcgui.NOTIFICATION_ERROR)
        return

    for nome, link in canais:
        li = xbmcgui.ListItem(nome)
        li.setInfo('video', {'title': nome})
        xbmcplugin.addDirectoryItem(handle, link, li, False)

    xbmcplugin.endOfDirectory(handle)

listar()
