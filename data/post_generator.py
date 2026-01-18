from llm import get_llm
from prepare_data import PrepareData

llm = get_llm()


def get_length(length):
    if length == "Short":
        return "1 to 5 lines"
    
    elif length == "Medium":
        return "5 to 10 lines"

    elif length == "Large":
        return "11 to 15 lines"
    
    else:
        return "2 to 8 lines"


def get_prompt(length, language, tag):
    prepare_data = PrepareData()
    lenght_str = get_length(length)
    prompt = f'''
    Generate a linkedin post using the below information. No preamble.
    1.Topic: {tag}
    2.length: {lenght_str}
    3.language: {language}
    If Language is Hinglish it means Hindi + English 
    The script for generating post is always English
    '''

    examples = prepare_data.get_filtered_posts(length, language, tag)
    if len(examples)>0:
        print("===============================================")
        prompt+=f"4. Use the writting style from the examples.\n5.The linebreak should follow the example."
        for i, post in enumerate(examples):
            post_text=post['text']
            prompt+=f"\n\n Exapmple {i+1}: \n\n {post_text}"

            if i==1:
                break
        print(prompt)
        print("==========================================")
    return prompt      

def generate_post(length, language, tag):
    
    prompt=get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    post = generate_post("Medium", "English", "Motivation")
    print(post)
    print("===============================================")