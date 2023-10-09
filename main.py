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
    # Регулярное выражение для поиска DOI
    doi_pattern = r'\b10\.\d{4,}/\S+\b'
    dois = re.findall(doi_pattern, file_contents)

    return dois


def get_udk(file_contents):
    # Регулярное выражение для поиска УДК-кодов
    udk_pattern = r'\d+(\.\d+)+'

    # Ищем первый УДК-код в строке
    udk = re.search(udk_pattern, file_contents)

    # Если найдено, возвращаем его, иначе возвращаем None
    if udk:
        return udk.group()
    else:
        return None
# def get_udk(file_contents):
#     # Регулярное выражение для поиска УДК
#     udk_pattern = r'\b\d+(\.\d+)+\b'
#     udks = re.findall(udk_pattern, file_contents)
#
#     return udks

def get_email(file_contents):
    # Регулярное выражение для поиска электронных адресов
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(email_pattern, file_contents)

    return emails


def extract_keywords(text):
    pattern = r'Ключевые\s*слова:\s*([^\.]+)\.'
    matches = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    if matches:
        keywords_text = matches.group(1)
        keywords_list = re.findall(r'\b\w+\b', keywords_text)
        return keywords_list
    else:
        return []
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

    found_degrees = []
    for regex, degree in degrees.items():
        result = re.search(regex, text)
        if result:
            found_degrees.append(degree)

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

