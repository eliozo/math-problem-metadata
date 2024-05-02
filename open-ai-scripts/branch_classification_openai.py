from openai import OpenAI
client = OpenAI()

def classify_math_problem(problem_text):
    """ Classify the type of math problem using OpenAI """
    prompt = f"Please find the branch of the math problem: \n\n '''{problem_text}'''\n\n" \
             " You can choose only one branch. Possible branches: " \
             "'Algebra'" \
             "'Geometry'" \
             "'NumberTheory'" \
             "'Combinatorics'"

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
    problem_text = """Let $n\geq 2$ be an integer and let $a_1, a_2, \ldots, a_n$ be positive real numbers with sum $1$. Prove that $$\sum_{k=1}^n \frac{a_k}{1-a_k}(a_1+a_2+\cdots+a_{k-1})^2 < \frac{1}{3}.$$
Let $m\ge 2$ be an integer, $A$ a finite set of integers (not necessarily positive) and $B_1,B_2,...,B_m$ subsets of $A$. Suppose that, for every $k=1,2,...,m$, the sum of the elements of $B_k$ is $m^k$. Prove that $A$ contains at least $\dfrac{m}{2}$ elements.
Let $n\geqslant 1$ be an integer, and let $x_0,x_1,\ldots,x_{n+1}$ be $n+2$ non-negative real numbers that satisfy $x_ix_{i+1}-x_{i-1}^2\geqslant 1$ for all $i=1,2,\ldots,n.$ Show that \[x_0+x_1+\cdots+x_n+x_{n+1}>\bigg(\frac{2n}{3}\bigg)^{3/2}.\]Pakawut Jiradilok and Wijit Yangjit, Thailand
Determine all functions $f: \mathbb{R} \rightarrow \mathbb{R}$ that satisfy $$(f(a)-f(b))(f(b)-f(c))(f(c)-f(a)) = f(ab^2+bc^2+ca^2) - f(a^2b+b^2c+c^2a)$$for all real numbers $a$, $b$, $c$."""

    # Classify the problem
    classify_math_problem(problem_text)

if __name__ == "__main__":
    main()