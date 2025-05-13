# main.py 25.0513

#1 ################################

#1.2

import markdown
from IPython.display import display, Markdown

# Example usage
markdown_text = """
# In‑N‑Out Burger Chatbot
"""

display(Markdown(markdown_text))

#1.3

import os
#from google.colab import userdata
#openai_api_key = userdata.get('OPENAI_API_KEY')
#os.environ['OPENAI_API_KEY'] = openai_api_key
# Verify that the key is set
#print(f"OpenAI API key set: {bool(openai_api_key)}")

# Retrieve the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Verify that the key is set
if openai_api_key:
    print("OpenAI API key successfully retrieved from environment variables.")
else:
    print("Error: OpenAI API key not found in environment variables.")

os.environ['OPENAI_API_KEY'] = openai_api_key

#1.4

import nest_asyncio
nest_asyncio.apply()

#1.5

MENU_PRICES = """

# In‑N‑Out Burger Menu (2025)

**Prices are approximate and subject to change.**

## Burgers & Combos

| Item                                    | Price  |
|-----------------------------------------|--------|
| Additional Burger Patty (per extra)     | $1.30  |
| Additional Cheese Slice (per extra)     | $0.50  |
| **Hamburger**                           | $3.60  |
| **Hamburger Combo**                     | $8.15  |
| **Cheeseburger**                        | $4.10  |
| **Cheeseburger Combo**                  | $8.65  |
| **Double Double®**                      | $5.90  |
| **Double Double® Combo**                | $10.45 |
| **French Fries**                        | $2.30  |

## Beverages

| Item                                        | Price  |
|---------------------------------------------|--------|
| **Coffee**                                  | $1.35  |
| **Hot Cocoa**                               | $2.25  |
| **Milk**                                    | $0.99  |
| **Shakes** (Chocolate, Strawberry, Vanilla) | $3.00  |
| **Soda (Small)**                            | $2.10  |
| **Soda (Medium)**                           | $2.25  |
| **Soda (Large)**                            | $2.45  |
| **Soda (X‑Large)**                          | $2.65  |

## Not‑So‑Secret Menu Options

- **Protein Style Burger:** Any burger wrapped in lettuce instead of a bun.
- **Animal Style:** Burger or fries served with a mustard‑cooked beef patty, extra spread, pickles, and grilled onions.

tax not included

tax is 7.25%

---"""

#1.6

from agents import Agent, Runner

agent = Agent(name="In-N-Out Cashier Assistant",
              instructions=f"You are a helpful server at In-N-Out Burger respond to questions based on the menu below: \n\n{MENU_PRICES}",
              model="gpt-4o"
              )

#1.7

result = Runner.run_sync(agent, "How much is a Double Double?.")
print(result.final_output)







