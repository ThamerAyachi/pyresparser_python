import re

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]


def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text


def retrieve_lists(data):
    skills = data.get('skills', [])
    experience = data.get('experience', [])
    return skills, experience


def merge_lists(skills, experience):
    return skills + experience


def has_more_than_three_numbers(item):
    numbers = re.findall(r'\d', item)
    return len(numbers) > 3


def contains_month_name(item):
    item_lower = item.lower()
    return any(month.lower() in item_lower for month in MONTHS)


def filter_lists(combined_list):
    filtered_list = []
    for item in combined_list:
        cleaned_item = clean_text(item)
        words = cleaned_item.split()
        if len(words) > 2:
            continue
        if has_more_than_three_numbers(cleaned_item):
            continue
        if contains_month_name(cleaned_item):
            continue
        filtered_list.append(' '.join(words))
    return filtered_list


def check_none_list(list):
    if list is not None:
        return list
    else:
        return []


def main(data):
    skills, experience = retrieve_lists(data)

    skills = check_none_list(skills)
    experience = check_none_list(experience)

    combined_list = merge_lists(skills, experience)
    filtered_list = filter_lists(combined_list)
    return filtered_list
