import speech_recognition as sr  # pip install SpeechRecognition
import whisper  # pip install whisper-openai
import pyttsx3  # pip install pyttsx3
import os
from PiscadaLoop import reproduzir_video_com_sprites


escolher_stt = "google"
# escolhe entrada por texto ou voz
entrada_por_texto = False
# falar ou nao
falar = True


if entrada_por_texto:
    sem_palavra_ativadora = True

def talk(texto):
    # falando
    engine.say(texto)
    engine.runAndWait()
    engine.stop()




def save_file(dados):
    with open(path + filename, "wb") as f:
        f.write(dados)
        f.flush()


# reconhecer
r = sr.Recognizer()
mic = sr.Microphone()
model = whisper.load_model("base")

# falar
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 215)  # velocidade 120 = lento
for indice, vozes in enumerate(voices):  # listar vozes
    print(indice, vozes.name)
    voz = 0
engine.setProperty('voice', voices[voz].id)


path = os.getcwd()
filename = "audio.wav"

print("Speak to Text", escolher_stt)

ajustar_ambiente_noise = True
reproduzir_video_com_sprites(caminho_video='Imagens_e_Vídeos/exemplo_de_sprites/Piscando.mp4')
talk("Olá, eu sou o Clevinho, e estou aqui pra tirar dúvidas sobre o Projeto da DevCrafters. Me Perguntem qualquer coisa!")
while True:
    text = ""
    question = ""
    try:
        if entrada_por_texto:
            question = input("Perguntar pro ChatGPT (\"sair\"): ")
        else:
            with mic as fonte:
                if ajustar_ambiente_noise:
                    r.adjust_for_ambient_noise(fonte)
                    ajustar_ambiente_noise = True
                print("Fale alguma coisa")
                audio = r.listen(fonte,phrase_time_limit=None)
                print("Enviando para reconhecimento")

            if escolher_stt == "google":
                question = r.recognize_google(audio, language="pt-BR")
            
    except sr.UnknownValueError:
     question = ''

    if "deslig" in question and "klebinho" in question or question.startswith("sair"):
        print(question, "Saindo.")
        if falar:
            talk("Desligando")
        break
    elif question == "":
        print("No sound")
        continue
    elif question.startswith("clebinho") or question.startswith("Clebinho") or question.startswith("klebinho") or question.startswith("Klebinho"):
        print("Me:", question)
        if "importância" in question:
             answer = 'Esse projeto é de extrema importância, \npois o uso de câmeras com scanner de rostos permite identificar\ne rastrear indivíduos suspeitos em tempo real.\nIsso facilita a intervenção rápida das autoridades\nem casos de sequestros de crianças,\naumentando as chances de resgates bem-sucedidos.'
             print("Steve:", answer)
             if falar:
                talk(answer)
        elif "funcionalidades" in question:
             answer = ' Essas câmeras são equipadas com algoritmos avançados de reconhecimento facial que podem\nidentificar e comparar rostos em tempo real com uma base de dados\nde pessoas suspeitas ou desaparecidas.\nAlém disso, elas possuem capacidades de monitoramento 24 horas por dia,\nsete dias por semana, e podem alertar automaticamente as autoridades competentes\nquando há uma possível correspondência.'
             print("Steve:", answer)
             if falar:
                talk(answer)
        elif "privacidade" in question:
             answer = 'A privacidade é uma preocupação central nesse projeto.\nTodas as imagens capturadas pelas câmeras são criptografadas e armazenadas de forma segura.\nAlém disso, apenas as autoridades responsáveis pelo monitoramento têm acesso aos dados.\nHá diretrizes e leis rigorosas em vigor para garantir que o uso dessas câmeras\nesteja em conformidade com as regulamentações de proteção de dados e privacidade.'
             print("Steve:", answer)
             if falar:
                talk(answer)
        elif "segurança" in question:
             answer = 'A integração com outros sistemas de segurança é fundamental\npara maximizar a eficiência desse projeto.\nAs câmeras programadas para scanner de rostos podem ser conectadas\na centrais de monitoramento e sistemas de alarme existentes.\nIsso permite que as informações identificadas pelas câmeras sejam transmitidas\nem tempo real para os operadores de segurança,\npossibilitando uma resposta imediata a qualquer incidente suspeito.'
             print("Steve:", answer)
             if falar:
                talk(answer)
        elif "benefícios" in question:
             answer = 'Além da prevenção de sequestros de crianças,\nesse projeto pode trazer vários benefícios adicionais.\nPor exemplo, ele pode ser útil na identificação de criminosos procurados,\najudando a reduzir a criminalidade em geral.\nAlém disso, o monitoramento contínuo por meio dessas câmeras pode proporcionar\numa sensação de segurança para a comunidade,\no que pode melhorar a qualidade de vida das pessoas\ne promover a confiança nas autoridades responsáveis pela segurança pública.'
             print("Steve:", answer)
             if falar:
                talk(answer)
        else :
             answer = 'Desculpa, eu não entendi muito bem'
             if falar:
                 talk(answer)
                 print("Clebinho:", answer)
            
    else:
        print("No message")
        continue