import openai

openai.api_key = "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"

prompt = "Once upon a time, in a small village nestled in a dense forest, there lived a young girl named Lily. She had long curly hair and bright blue eyes. Lily was known for her kindness and her love of adventure. One day, while exploring the woods, Lily stumbled upon an old cottage that she had never seen before."


def correct_grammar(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Please correct the grammar in the following text:\n{text}\n---\n"),
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=15,
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return text


def generate_story(prompt):
    length = 500
    temperature = 0.5

    # Generate the story using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=length,
        temperature=temperature
    )

    story = response.choices[0].text
    story = story.replace("\n", " ")
    story = story.strip()
    story = story.capitalize()

    return story

story = generate_story(prompt)

story = correct_grammar(story)
print(story)
with open("story.txt", "w") as file:
    file.write(story)