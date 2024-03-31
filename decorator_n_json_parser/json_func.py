import json


def keyword_callback(keyword, field):
    print(f"Keyword {keyword} was found in {field}")


def parse_json(
    json_str: str, required_fields=None, keywords=None, keyword_callback=None
):
    if required_fields is None:
        required_fields = []
    if keywords is None:
        keywords = []
    if keyword_callback is None:
        keyword_callback = lambda keyword, field: None

    json_doc = json.loads(json_str)
    for field in required_fields:
        if field in json_doc.keys() and isinstance(field, str):
            for keyword in keywords:
                keyword_list = json_doc[field].split()
                for word in keyword_list:
                    if keyword.casefold() in word.casefold() and isinstance(
                        keyword, str
                    ):
                        keyword_callback(keyword, field)


if __name__ == "__main__":
    parse_json(
        '{"key1": "Word1 word2", "key2": "word2 word3"}',
        ["Key1", "key2"],
        ["word1", "WORD3", "word2"],
        keyword_callback,
    )
