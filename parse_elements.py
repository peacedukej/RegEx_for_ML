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
    # Регулярное выражение для поиска УДК
    udk_pattern = r'\b\d+(\.\d+)+\b'
    udks = re.findall(udk_pattern, file_contents)

    return udks

def get_email(file_contents):
    # Регулярное выражение для поиска электронных адресов
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(email_pattern, file_contents)

    return emails


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
        print(file_contents)
        get_doi(file_contents)
        get_udk(file_contents)
        #get_email(file_contents)
        #get_keywords(file_contents)
