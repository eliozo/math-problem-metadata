from openai import OpenAI
client = OpenAI()

def classify_math_problem(problem_text,problem_solution):
    """ Classify the type of math problem using OpenAI """
    prompt = "Imagine that you are IMO problem selection committee member - and you are selecting problems for the International Math Olympiad." \
"Your task is to find the most appropriate topic for each problem we specify - whether it is Algebra, Combinatorics, Geometry or Number Theory." \
             "Geometry: Geometry problems in math olympiads often involve creative problem-solving using principles " \
             "of Euclidean geometry. These problems may require the use of geometric properties, theorems, " \
             "and constructions to prove statements or find unknown quantities." \
             "Algebra: Algebra problems typically involve the manipulation and analysis of equations, inequalities, " \
             "and algebraic" \
            "expressions. These problems may require techniques such as factorization, substitution, manipulation " \
             "of " \
              "polynomials, and the application of algebraic identities." \
             "Number Theory: Number theory problems focus on properties and relationships of integers." \
             "These problems often involve divisibility, prime numbers, modular arithmetic, and properties of " \
             "sequences and series." \
             "Combinatorics: Combinatorics problems deal with counting, arranging, and selecting objects. These " \
             "problems may " \
             "involve permutations, combinations, pigeonhole principle, graph theory, and other counting principles." \
             f"Here is a problem you would need to classify: \n\n'''{problem_text}'''\n\n and here is a solution for " \
             f"this problem, that would help you to decide how to classify the problem: \n\n ''" \
             f"'{problem_solution}'''\n\n"


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
    problem_text = """
Let $n$ be a positive integer. Given is a subset $A$ of $\{0,1,...,5^n\}$ with $4n+2$ elements. Prove that there exist three elements $a<b<c$ from $A$ such that $c+2a>3b$.
"""
    problem_solution = """"Solution 1. (By contradiction) Suppose that there exist 4n ` 2 non-negative integers x0 ă
x1 ă ¨ ¨ ¨ ă x4n`1 that violate the problem statement. Then in particular x4n`1 ` 2xi ď 3xi`1
for all i “ 0, . . . , 4n ´ 1, which gives
x4n`1 ´ xi ě
3
2
px4n`1 ´ xi`1q.
By a trivial induction we then get
x4n`1 ´ xi ě
ˆ
3
2
˙4n´i
px4n`1 ´ x4nq,
which for i “ 0 yields the contradiction
x4n`1 ´ x0 ě
ˆ
3
2
˙4n
px4n`1 ´ x4nq “ ˆ
81
16˙n
px4n`1 ´ x4nq ą 5
n
¨ 1"""

    # Classify the problem
    classify_math_problem(problem_text,problem_solution)

if __name__ == "__main__":
    main()