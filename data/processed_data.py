import json
from llm import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

def processed_data(raw_file_path, processed_file_path="processed_data.json"):
    enriched_post=[]
    with open(raw_file_path, encoding='utf-8') as file:
        posts= json.load(file)
        for post in posts:
            metadata=extract_metadata(post["text"])
            post_with_metadata= post | metadata
            enriched_post.append(post_with_metadata)

    unified_tags=get_unified_tags(enriched_post)

    for post in enriched_post:
        current_tags = post['tags']
        new_tags= {unified_tags[tag] for tag in current_tags}
        post['tags']=list(new_tags)

    with open(processed_file_path, encoding='utf-8',mode='w') as outfile:
        json.dump(enriched_post, outfile, indent=4)


def get_unified_tags(post_with_metadata):
    unique_tags=set()
    for post in post_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list=','.join(unique_tags)

    template= '''
    I'll give you a list of tags. You need to unify tags with the following reauirments,
    1.Tags are unified and merged to create a shorter list.append
    Example 1: "JobSeeker","Job Hunting" can all be merged into a single tag "Job Search".
    Example 2: 'MOtivation',"Inspiration", "Drive" can be mapped to "Motivation"
    Example 3: "Personal Growth", "Personal Devlopement" can be mappe to "Personal Engagement"
    2.Each tag should be follow title case convention. Eample: 'Motivation', 'Job Search'
    3.Output should be JSON obect. No preamble.
    4.Output should have mapping of original tag and the unified unique_tags
    For Example: {{"JobSeeker":"Job Search","Job Hunting":"Job Search", "Motivation":"Motivation"}}

    Here is the list of tags:
    {tags}
    '''

    pt= PromptTemplate.from_template(template)
    chain = pt | llm
    response= chain.invoke(input={"tags": unique_tags_list})

    json_parser=JsonOutputParser()
    res=json_parser.parse(response.content)

    return res

def extract_metadata(post):
    template='''
    You are given a linkedin post. You need to expract number of lines, language of the post and tags
    1.Return a valid JSON. No preamble.
    2.JSON Object should have exactly three keys: line_count, language and tags.
    3.tags is an array of text tags. Extract maximum 2 tags.
    4.Language should be English or Hinglish (Hinglish means hindi+English)

    Here is the actual post on which you need to perform this task: {post}
    '''

    pt=PromptTemplate.from_template(template)
    chain= pt | llm
    response=chain.invoke(input={'post':post})

    json_parser=JsonOutputParser()
    res=json_parser.parse(response.content)

    return res


if __name__ == "__main__":
    processed_data("raw_data.json","processed_data.json")



