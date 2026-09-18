# Rule-Based Customer Support Chatbot

This project demonstrates a simple **rule-based customer support chatbot** built with Python and the **NLTK** library.

The chatbot uses predefined patterns to recognize common user queries and provide appropriate responses.

## What This Script Does

1. Accepts input from the user.
2. Matches the input against predefined patterns.
3. Returns a predefined response.
4. Continues the conversation until the user types `quit`.

## Example Responses

| User Input  | Chatbot Response                                            |
| ----------- | ----------------------------------------------------------- |
| `need help` | Sure, how can I assist you?                                 |
| `price of`  | The price of the item is $50.                               |
| `courses`   | Provides information about DevOps and Cloud DevOps courses. |
| `quit`      | Goodbye! Have a great day.                                  |

## Technologies Used

* Python
* NLTK
* `Chat`
* `reflections`
* Regular expressions

## How It Works

```text
User Input
    ↓
Pattern Matching
    ↓
Find Matching Rule
    ↓
Return Response
    ↓
Continue Conversation
```

## Setup

### 1. Install NLTK

```bash
pip install nltk
```

### 2. Run the Script

```bash
python chatbot.py
```

## Example

```text
Welcome to Customer Support. Type 'quit' to exit.

User: need help
Bot: Sure, how can I assist you?

User: courses
Bot: If you are looking for DevOps and Cloud DevOps courses, check out devopsshack.com.

User: quit
Bot: Goodbye! Have a great day.
```

## Purpose

This project demonstrates the basics of **rule-based automation, pattern matching, and conversational interfaces using Python**.
