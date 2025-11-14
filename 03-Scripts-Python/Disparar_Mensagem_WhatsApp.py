import json
import xml.etree.ElementTree as ET

# 1. DEFININDO AS FONTES DE ANÚNCIO (Origem dos dados)

class FonteAnuncio:
    """Classe base abstrata para fontes de anúncio."""
    def obter_anuncio(self):
        raise NotImplementedError("Método 'obter_anuncio' deve ser implementado pela classe concreta")

class BancoDadosFonte(FonteAnuncio):
    def obter_anuncio(self):
        # Simula a busca de um banco de dados
        return {"titulo": "Promoção Imperdível", "mensagem": "Desconto de 50%! Não perca!"}

class JSONFonte(FonteAnuncio):
    def obter_anuncio(self):
        anuncio_json = '{"titulo": "Promoção Imperdível", "mensagem": "Desconto de 50%! Não perca!"}'
        return json.loads(anuncio_json)

class XMLFonte(FonteAnuncio):
    def obter_anuncio(self):
        anuncio_xml = """<anuncio><titulo>Promoção Imperdível</titulo><mensagem>Desconto de 50%! Não perca!</mensagem></anuncio>"""
        root = ET.fromstring(anuncio_xml)
        return {"titulo": root.find('titulo').text, "mensagem": root.find('mensagem').text}

class TextoFonte(FonteAnuncio):
    def obter_anuncio(self):
        # Simula a leitura de um arquivo de texto simples
        return {"titulo": "Promoção Imperdível", "mensagem": "Desconto de 50%! Não perca!"}

# 2. DEFININDO OS DESTINOS DE ANÚNCIO (Para onde vai)

class DestinoAnuncio:
    """Classe base abstrata para destinos de anúncio."""
    def enviar_anuncio(self, anuncio):
        raise NotImplementedError("Método 'enviar_anuncio' deve ser implementado pela classe concreta")

class WhatsAppDestino(DestinoAnuncio):
    def enviar_anuncio(self, anuncio):
        print(f"Enviando anúncio para WhatsApp: {anuncio['titulo']} - {anuncio['mensagem']}")

class SMSDestino(DestinoAnuncio):
    def enviar_anuncio(self, anuncio):
        print(f"Enviando SMS: {anuncio['titulo']} - {anuncio['mensagem']}")

class FacebookDestino(DestinoAnuncio):
    def enviar_anuncio(self, anuncio):
        print(f"Enviando anúncio para Facebook: {anuncio['titulo']} - {anuncio['mensagem']}")


# 3. CLASSE DE ORQUESTRAÇÃO (Onde a lógica acontece)


class AnuncioHandler:
    """Orquestra o fluxo de obter, editar e enviar o anúncio."""
    def __init__(self, fonte: FonteAnuncio, destino: DestinoAnuncio):
        self.fonte = fonte
        self.destino = destino

    def processar_anuncio(self):
        # 1. Obter o anúncio
        anuncio = self.fonte.obter_anuncio()
        
        print("\n--- Anúncio Original ---")
        print(f"Título: {anuncio['titulo']}")
        print(f"Mensagem: {anuncio['mensagem']}")

        # 2. Editar o anúncio (A função 'editar_anuncio' modifica o dicionário)
        editar_anuncio(anuncio) 

        # 3. Enviar o anúncio (agora modificado)
        print("\n--- Enviando Anúncio Editado ---")
        self.destino.enviar_anuncio(anuncio)

# 4. FACTORY (Para criar os objetos)

class AnuncioFactory:
    """Factory para criar instâncias de fontes e destinos."""
    @staticmethod
    def criar_fonte(tipo_fonte: str) -> FonteAnuncio:
        if tipo_fonte == "banco":
            return BancoDadosFonte()
        elif tipo_fonte == "json":
            return JSONFonte()
        elif tipo_fonte == "xml":
            return XMLFonte()
        elif tipo_fonte == "texto":
            return TextoFonte()
        else:
            raise ValueError(f"Fonte desconhecida: {tipo_fonte}")

    @staticmethod
    def criar_destino(tipo_destino: str) -> DestinoAnuncio:
        if tipo_destino == "whatsapp":
            return WhatsAppDestino()
        elif tipo_destino == "sms":
            return SMSDestino()
        elif tipo_destino == "facebook":
            return FacebookDestino()
        else:
            raise ValueError(f"Destino desconhecido: {tipo_destino}")

# 5. FUNÇÕES AUXILIARES E PRINCIPAL

def editar_anuncio(anuncio):
    """Modifica o dicionário do anúncio com base no input do usuário."""
    print("\nVocê pode editar o anúncio completo!")
    novo_titulo = input(f"Digite o novo título do anúncio (Atual: {anuncio['titulo']}): ")
    nova_mensagem = input(f"Digite a nova mensagem do anúncio (Atual: {anuncio['mensagem']}): ")

    # Atualizando o anúncio com os novos valores, se fornecidos
    if novo_titulo.strip():  # Verifica se o novo título não está vazio
        anuncio["titulo"] = novo_titulo
    if nova_mensagem.strip():  # Verifica se a nova mensagem não está vazia
        anuncio["mensagem"] = nova_mensagem
    
    print("Anúncio atualizado.")

# 6. FUNÇÃO PRINCIPAL (Execução)

def main():
    print("Escolha a fonte do anúncio:")
    print("1. Banco de Dados")
    print("2. JSON")
    print("3. XML")
    print("4. Texto")
    escolha_fonte = input("Digite o número correspondente à fonte (1-4): ")

    if escolha_fonte == '1':
        fonte = AnuncioFactory.criar_fonte("banco")
    elif escolha_fonte == '2':
        fonte = AnuncioFactory.criar_fonte("json")
    elif escolha_fonte == '3':
        fonte = AnuncioFactory.criar_fonte("xml")
    elif escolha_fonte == '4':
        fonte = AnuncioFactory.criar_fonte("texto")
    else:
        print("Opção inválida. Usando a fonte padrão (Texto).")
        fonte = AnuncioFactory.criar_fonte("texto")

    print("\nEscolha o destino do anúncio:")
    print("1. WhatsApp")
    print("2. SMS")
    print("3. Facebook")
    escolha_destino = input("Digite o número correspondente ao destino (1-3): ")

    if escolha_destino == '1':
        destino = AnuncioFactory.criar_destino("whatsapp")
    elif escolha_destino == '2':
        destino = AnuncioFactory.criar_destino("sms")
    elif escolha_destino == '3':
        destino = AnuncioFactory.criar_destino("facebook")
    else:
        print("Opção inválida. Usando o destino padrão (WhatsApp).")
        destino = AnuncioFactory.criar_destino("whatsapp")

    # Criando o handler
    handler = AnuncioHandler(fonte, destino)

    # Processar o anúncio (agora o handler cuida de obter, editar e enviar)
    handler.processar_anuncio()

if __name__ == "__main__":
    main()
