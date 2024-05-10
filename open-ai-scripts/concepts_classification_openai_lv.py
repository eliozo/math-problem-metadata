from openai import OpenAI
client = OpenAI()
import re

def normalize_text(text):
    text = re.sub(r'\$[^\$]+?\$', '_EXPR_', text)  # Aizstāj formulas ar _EXPR_
    text = re.sub(r'[^\w\s\.\?!]', '', text)  # Izdzēš simbolus, kas nav burti, cipari vai .,?,!
    text = re.sub(r'\s+', ' ', text).strip()  # Aizstāj daudzus tukšumus ar vienu tukšumu
    return text

def classify_math_problem(problem_text):
    problem_text = normalize_text(problem_text)  # Normalize the problem text
    """ Classify the type of math problem using OpenAI """
    prompt = "Iedomājieties, ka esat IMO problēmu atlases komisijas loceklis - un jūs izvēlaties uzdevumu terminus " \
             "Starptautiskajai Matemātikas olimpiādei." \
            f"Šeit ir problēma, kurā jums būtu jāatrod termini: \n\n'''{problem_text}'''\n\n"


    response = client.chat.completions.create(
      model="gpt-4-turbo",
      response_format={ "type": "text" },
      messages=[
        {"role": "system", "content": "Tu esi izpalīdzīgs asistents, kurš izdod atbildi teksta formātā, "
                                      "katru terminu atdalot ar komatu."},
        {"role": "user", "content": prompt}
      ]
    )
    print(response.choices[0].message.content)

def main():

    # User input
    problem_text = """
Dots, ka $a,b,c,d$ – naturāli skaitļi un $ab=cd$. Pierādīt, ka skaitli $a^2 + b^2 + c^2 + d^2$ 
var izsacīt kā divu veselu skaitļu kvadrātu summu. Vai to noteikti var izsacīt kā divu naturālu skaitļu kvadrātu summu?
"""

    # Classify the problem
    classify_math_problem(problem_text)

if __name__ == "__main__":
    main()