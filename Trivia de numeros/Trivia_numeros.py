def main():
  print("Hello learners!")

import requests

def trivia_fetch(num):
    """
    Llama a la API de Numbers y devuelve un diccionario con trivia sobre el número.
    """
    url = f"http://numbersapi.com/{num}?json"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    print("Hola Curiosos de los números, bienvenidos al quiz de números ✨")
    numero = int(input("Escribe un número para ver un dato curioso: "))
    trivia = trivia_fetch(numero)
    print(f"Dato sobre {trivia['number']}: {trivia['text']}")

if __name__ == "__main__":
    main()
