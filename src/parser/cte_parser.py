import xml.etree.ElementTree as ET

def get_text_or_none(root, path, ns):
    """Tenta buscar o campo XML, retorna None se não existir"""
    element = root.find(path, ns)
    return element.text if element is not None else None

def extrair_dados_cte(file_path):
    ns = {"ns": "http://www.portalfiscal.inf.br/cte"}
    tree = ET.parse(file_path)
    root_xml = tree.getroot()

    dados = {
        # Origem/Destino
        "cMunIni": get_text_or_none(root_xml, ".//ns:cMunIni", ns),
        "xMunIni": get_text_or_none(root_xml, ".//ns:xMunIni", ns),
        "UFIni": get_text_or_none(root_xml, ".//ns:UFIni", ns),
        "cMunFim": get_text_or_none(root_xml, ".//ns:cMunFim", ns),
        "xMunFim": get_text_or_none(root_xml, ".//ns:xMunFim", ns),
        "UFFim": get_text_or_none(root_xml, ".//ns:UFFim", ns),

        # CFOP
        "CFOP": get_text_or_none(root_xml, ".//ns:CFOP", ns),

        # Emitente
        "Emitente CNPJ": get_text_or_none(root_xml, ".//ns:emit/ns:CNPJ", ns),
        "Emitente Nome": get_text_or_none(root_xml, ".//ns:emit/ns:xNome", ns),

        # Remetente
        "Remetente CNPJ": get_text_or_none(root_xml, ".//ns:rem/ns:CNPJ", ns),
        "Remetente Nome": get_text_or_none(root_xml, ".//ns:rem/ns:xNome", ns),

        # Destinatário
        "Destinatário CNPJ": get_text_or_none(root_xml, ".//ns:dest/ns:CNPJ", ns),
        "Destinatário Nome": get_text_or_none(root_xml, ".//ns:dest/ns:xNome", ns),

        # Valores de prestação
        "vTPrest": get_text_or_none(root_xml, ".//ns:vPrest/ns:vTPrest", ns),
        "vRec": get_text_or_none(root_xml, ".//ns:vPrest/ns:vRec", ns),

        # ICMS (tratando variações)
        "vBC": get_text_or_none(root_xml, ".//ns:imp/ns:ICMS/ns:ICMS00/ns:vBC", ns) or \
               get_text_or_none(root_xml, ".//ns:imp/ns:ICMS/ns:ICMSOutraUF/ns:vBCOutraUF", ns),
        "pICMS": get_text_or_none(root_xml, ".//ns:imp/ns:ICMS/ns:ICMS00/ns:pICMS", ns) or \
                 get_text_or_none(root_xml, ".//ns:imp/ns:ICMS/ns:ICMSOutraUF/ns:pICMSOutraUF", ns),
        "vICMS": get_text_or_none(root_xml, ".//ns:imp/ns:ICMS/ns:ICMS00/ns:vICMS", ns) or \
                 get_text_or_none(root_xml, ".//ns:imp/ns:ICMS/ns:ICMSOutraUF/ns:vICMSOutraUF", ns),

        # Chave da NF-e vinculada
        "Chave NF-e": get_text_or_none(root_xml, ".//ns:infNFe/ns:chave", ns),

        # Observação
        "xObs": get_text_or_none(root_xml, ".//ns:xObs", ns)
    }

    return dados
