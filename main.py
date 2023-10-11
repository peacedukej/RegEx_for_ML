import re

"""
Структурные элементы для автоматического распознавания:

    doi                                             |
    удк                                             |

    ФИО (name)                                      |
    e-mail                                          |
    ученая степень (degree)* (список)               |
    должность (position)* (как ученая степень)      |

    название (title)                                |
    город (city)                                    |
    том (volume)                                    |
    выпуск (issue)                                  |
    раздел/рубрика/секция (section)                 |
    страницы (pages) (автоматический)               |
    издательство (publisher)                        |
    год издания (year)                              |

    ключевые слова (keywords) (автоматический )     |
    аннотация (annotation) (полуавтоматически)      |

"""

"""
Сначала читается файл txt

"""


def get_doi(file_contents):
    doi_pattern = r'\b10\.\d{4,}/\S+\b'
    matches = re.finditer(doi_pattern, file_contents)
    results = {}

    for match in matches:
        start_line = file_contents.count('\n', 0, match.start()) + 1
        end_line = file_contents.count('\n', 0, match.end()) + 1
        #results.add((match.group(), [start_line, end_line]))
        results['doi'] = [start_line, end_line]

    return results


def get_udk(file_contents):
    udk_pattern = r'\d+(\.\d+)+'
    udk_match = re.search(udk_pattern, file_contents)
    results = {}
    if udk_match:
        start_line = file_contents.count('\n', 0, udk_match.start()) + 1
        end_line = file_contents.count('\n', 0, udk_match.end()) + 1
        results['udk'] = [start_line, end_line]
        return results
        #return [(udk_match.group(), start_line, end_line)]
    else:
        return None
# def get_udk(file_contents):
#     # Регулярное выражение для поиска УДК
#     udk_pattern = r'\b\d+(\.\d+)+\b'
#     udks = re.findall(udk_pattern, file_contents)
#
#     return udks

def get_email(file_contents):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_matches = re.finditer(email_pattern, file_contents)
    email_results = {}

    for match in email_matches:
        start_line = file_contents.count('\n', 0, match.start()) + 1
        end_line = file_contents.count('\n', 0, match.end()) + 1
        email_results['email'] = [start_line, end_line]
        #email_results.append((match.group(), start_line, end_line))

    return email_results

def extract_keywords(text):
    pattern = r'Ключевые\s*слова:\s*([^\.]+)\.'
    matches = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    keyword_results = {}

    if matches:
        keywords_text = matches.group(1)
        keywords_list = re.findall(r'\b\w+\b', keywords_text)

        if keywords_list:
            start = text.find(keywords_list[0])
            end = text.rfind(keywords_list[-1]) + len(keywords_list[-1])
            start_line = text.count('\n', 0, start) + 1
            end_line = text.count('\n', 0, end) + 1
            keyword_results['keywords'] = [start_line, end_line]
            #keyword_results.append((keywords_list, start_line, end_line))

    return keyword_results


# def extract_keywords(text):
#     pattern = r'Ключевые\s*слова:\s*([^\.]+)\.'
#     matches = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
#     if matches:
#         keywords_text = matches.group(1)
#         keywords_list = re.findall(r'\b\w+\s*-\s*\w+:\s*[^,]+', keywords_text)
#         return keywords_list
#     else:
#         return []


def get_degree(text):
    degrees = {
        r'д\.арх\.н\.': 'д.арх.н.',
        r'к\.арх\.н\.': 'к.арх.н.',
        r'д\.б\.н\.': 'д.б.н.',
        r'к\.б\.н\.': 'к.б.н.',
        r'д\.в\.н\.': 'д.в.н.',
        r'к\.в\.н\.': 'к.в.н.',
        r'д\.воен\.н\.': 'д.воен.н.',
        r'к\.воен\.н\.': 'к.воен.н.',
        r'д\.г\.н\.': 'д.г.н.',
        r'к\.г\.н\.': 'к.г.н.',
        r'д\.г\.-м\.н\.': 'д.г.-м.н.',
        r'к\.г\.-м\.н\.': 'к.г.-м.н.',
        r'д\.иск\.': 'д.иск.',
        r'к\.иск\.': 'к.иск.',
        r'д\.и\.н\.': 'д.и.н.',
        r'к\.и\.н\.': 'к.и.н.',
        r'д\.м\.н\.': 'д.м.н.',
        r'к\.м\.н\.': 'к.м.н.',
        r'д\.п\.н\.': 'д.п.н.',
        r'к\.п\.н\.': 'к.п.н.',
        r'д\.пол\.н\.': 'д.пол.н.',
        r'к\.пол\.н\.': 'к.пол.н.',
        r'д\.псх\.н\.': 'д.псх.н.',
        r'к\.псх\.н\.': 'к.псх.н.',
        r'д\.с\.-х\.н\.': 'д.с.-х.н.',
        r'к\.с\.-х\.н\.': 'к.с.-х.н.',
        r'д\.соц\.н\.': 'д.соц.н.',
        r'к\.соц\.н\.': 'к.соц.н.',
        r'д\.т\.н\.': 'д.т.н.',
        r'к\.т\.н\.': 'к.т.н.',
        r'д\.фарм\.н\.': 'д.фарм.н.',
        r'к\.фарм\.н\.': 'к.фарм.н.',
        r'д\.ф\.-м\.н\.': 'д.ф.-м.н.',
        r'к\.ф\.-м\.н\.': 'к.ф.-м.н.',
        r'д\.филол\.н\.': 'д.филол.н.',
        r'к\.филол\.н\.': 'к.филол.н.',
        r'д\.филос\.н\.': 'д.филос.н.',
        r'к\.филос\.н\.': 'к.филос.н.',
        r'д\.х\.н\.': 'д.х.н.',
        r'к\.х\.н\.': 'к.х.н.',
        r'д\.э\.н\.': 'д.э.н.',
        r'к\.э\.н\.': 'к.э.н.',
        r'д\.ю\.н\.': 'д.ю.н.',
        r'к\.ю\.н\.': 'к.ю.н.',
    }

    found_degrees = {}
    for regex, degree in degrees.items():
        results = re.finditer(regex, text)
        for result in results:
            start_line = text.count('\n', 0, result.start()) + 1
            end_line = text.count('\n', 0, result.end()) + 1
            #found_degrees.append((degree, start_line, end_line))
            found_degrees['degree'] = [start_line, end_line]

    return found_degrees


def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        return f"Файл '{filename}' не найден."
    except Exception as e:
        return f"Произошла ошибка при чтении файла: {e}"



if __name__ == "__main__":
    filename = 'text.txt'
    file_contents = read_text_file(filename)
    if file_contents is not None:

        print(get_doi(file_contents))

        print(get_udk(file_contents))

        print(extract_keywords(file_contents))
        # keywords = []
        # for item in extract_keywords(file_contents):
        #     # Разделяем элемент по символам новой строки и добавляем каждое слово в список
        #     words = item.split('\n')
        #     for word in words:
        #         cleaned_word = re.sub(r'[^\w-]', '', word)
        #         keywords.append(cleaned_word)
        # print(keywords)
        print(get_email(file_contents))
        print(get_degree(file_contents))

