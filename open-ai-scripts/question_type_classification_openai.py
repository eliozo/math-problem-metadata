from openai import OpenAI
client = OpenAI()

def classify_math_problem(problem_text):
    """ Classify the type of math problem using OpenAI """
    prompt = f"Lūdzu atrodi matemātikas uzdevuma tipu: \n\n '''{problem_text}'''\n\n" \
             " Iespējamie jautājumu tipi ir: " \
             "'Find.All' (uzdevumi, kuros jāatrod visi atrisinājumi); " \
             "'Find.Count' (uzdevumi, kuros jāsaskaita iespēju vai atrisinājumu skaits); " \
             "'Find.Optimal' (uzdevumi, kuros jāatrod maksimālais vai minimālais risinājums); " \
             "'Find.Example' (uzdevumi, kuros jāatrod 1 piemērs vai pretpiemērs); " \
             "'Prove' (uzdevumi, kuros jāpierāda apgalvojums); " \
             "'ProveDisprove' (uzdevumi, kuros apgalvojums ir jāpierāda vai jāapgāž); " \
             "'Algorithm' (uzdevumi, kuros jāatrod procedūra vai spēles stratēģija)."

    response = client.chat.completions.create(
      model="gpt-4-turbo",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": prompt}
      ]
    )
    print(response.choices[0].message.content)


def main():

    # User input
    problem_text = """Kādām naturālām $n$ vērtībām var atrast $2n+1$ naturālus skaitļus (ne obligāti dažādus) 
ar īpašību, ka, izvēloties jebkurus $n+1$ no tiem, to summa dalīsies ar atlikušo $n$ 
skaitļu summu?"""

    # Classify the problem
    classify_math_problem(problem_text)


if __name__ == "__main__":
    main()

