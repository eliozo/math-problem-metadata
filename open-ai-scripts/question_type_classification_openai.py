from openai import OpenAI
client = OpenAI()

def classify_math_problem(problem_text):
    """ Classify the type of math problem using OpenAI """
    prompt = f"Lūdzu atrodi matemātikas uzdevuma tipu: \n\n '''{problem_text}'''\n\n" \
             " Iespējamie jautājumu tipi ir: " \
             "'Find.All' (uzdevumi, kuros jāatrod visi atrisinājumi); " \
             "'Find.Count' (uzdevumi, kuros jāsaskaita cik iespēju vai atrisinājumu skaits); " \
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
    problem_text = """Uz tāfeles pa reizei uzrakstīti visi naturālie skaitļi no $1$ līdz $n$ ieskaitot. 
Ar vienu gājienu var izvēlēties divus uz tāfeles uzrakstītus skaitļus 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt $\left| a^2-b^2 \right|$. 
Pēc $n-1$ gājiena uz tāfeles paliek viens skaitlis.  
Vai tas var būt $0$, ja **(a)** $n=8$, **(b)** $n=9$?"""

    # Classify the problem
    classify_math_problem(problem_text)


if __name__ == "__main__":
    main()

