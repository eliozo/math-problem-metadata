from openai import OpenAI
client = OpenAI()

def classify_math_problem(problem_text):
    """ Classify the type of math problem using OpenAI """
    prompt = "Iedomājieties, ka esat IMO problēmu atlases komisijas loceklis - un jūs izvēlaties problēmas Starptautiskajai Matemātikas olimpiādei." \
            "Jūsu uzdevums ir atrast vispiemērotāko tēmu katrai problēmai, ko mēs norādām - vai nu tā būtu algebra, kombinatorika, ģeometrija vai skaitļu teorija." \
            "Ģeometrija: Ģeometrijas problēmas matemātikas olimpiādēs bieži vien ietver radošu problēmu risināšanu, izmantojot Eiklīda ģeometrijas principus. " \
            "Šīs problēmas var prasīt ģeometrisko īpašību, teorēmu un konstrukciju izmantošanu, lai pierādītu apgalvojumus vai atrastu nezināmas lielumus." \
            "Algebra: Algebras problēmas parasti ietver vienādojumu, nevienādojumu un algebrisku izteiksmju manipulēšanu un analīzi. " \
            "Šīs problēmas var prasīt tehniskus paņēmienus, piemēram, faktorizāciju, substitūciju, polinomu manipulēšanu un algebrisku identitāšu piemērošanu." \
            "Skaitļu teorija: Skaitļu teorijas problēmas koncentrējas uz veselu skaitļu īpašībām un attiecībām." \
            "Šīs problēmas bieži ietver dalāmību, pirmskaitļus, modulāro aritmetiku un secību un sēriju īpašības." \
            "Kombinatorika: Kombinatorikas problēmas nodarbojas ar objektu skaitīšanu, sakārtošanu un izvēli. " \
            "Šīs problēmas var ietvert permutācijas, kombinācijas, 'vistu būrīša' principu, grafu teoriju un citus skaitīšanas principus." \
            f"Šeit ir problēma, kuru jums būs jāklasificē: \n\n'''{problem_text}'''\n\n"


    response = client.chat.completions.create(
      model="gpt-4-turbo",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "Tu esi izpalīdzīgs asistents, kurš izdod atbildi JSON formātā."},
        {"role": "user", "content": prompt}
      ]
    )
    print(response.choices[0].message.content)


def main():

    # User input
    problem_text = """
Dota rūtiņu tabula $n \times n$. Ilmārs un Kims spēlē šādu spēli. Viņi pēc kārtas kādā vēl tukšā rūtiņā ieraksta skaitli $1$
vai $-1$. Spēli sāk Ilmārs. Ja pēc kāda spēlētāja gājiena tiek aizpildīta kāda rinda vai kolonna, tad tiek aprēķināts
tajā esošo skaitļu reizinājums. Ja tas ir vienāds ar $-1$, tad spēlētājs, kurš veica pēdējo gājienu, iegūst $1$ punktu
(ja spēlētājs ar savu gājienu vienlaicīgi pabeidz gan rindu, gan kolonnu un katrā skaitļu reizinājums ir $-1$, tad
viņš iegūst divus punktus). Spēle beidzas, kad tabula ir pilnībā aizpildīta. Uzvar spēlētājs, kurš iegūst visvairāk
punktu. Kuram spēlētājam ir uzvaroša stratēģija, ja **(a)** $n = 2021$; **(b)**  $n = 2022$?
"""

    # Classify the problem
    classify_math_problem(problem_text)

if __name__ == "__main__":
    main()