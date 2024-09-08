
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# utils.py
def str_shelfs():
    """
    :return: A list of all the shelfs in the directories.
    """
    directories_str = ', '.join(directories.keys())
    return directories_str


def doc_owner(number):
    """
    :param number: The document number to search for.
    :return: The name of the document owner if the document is found,
    otherwise a string indicating that the document is not found.
    """
    for document in documents:
        if document['number'] == number:
            return f"Владелец документа:{document['name']}"
    return "Документ не найден в базе"


def document_shelf(number):
    """
    :param number: The document number to search for within the directories.
    :return: A message indicating the shelf on which the document is stored
    or a message stating that the document was not found.
    """
    for shelf, documents in directories.items():
        if number in documents:
            return f"Документ хранится на полке: {shelf}"
    return "Документ не найден в базе"


def all_info_about_docs():
    """
    Displays information about all documents, including their number, type, owner,
    and the shelf where they are stored.
    :return: None
    """
    for document in documents:
        doc_number = document['number']
        doc_type = document['type']
        doc_own = document['name']
        shelf = document_shelf(doc_number).split("Документ хранится на полке:")[1].strip()
        print(f"№: {doc_number}, тип: {doc_type}, владелец: {doc_own}, полка хранения: {shelf}")


def add_shelf(number):
    """
    :param number: The number identifying the shelf to be added.
    :return: None.
    """
    if str(number) in directories:
        print("Полка уже существует")
    else:
        directories[str(number)] = []
        print(f"Полка добавлена. Текущий уровень полок: {str_shelfs()}.")


def delete_shelf(number):
    """
    :param number: The number identifying the shelf to be deleted.
    :return: None.
    """
    if str(number) in directories and len(directories[str(number)]) == 0:
        del directories[str(number)]
        print(f"Полка удалена. Текущий уровень полок: {str_shelfs()}.")
    elif str(number) not in directories:
        print("Полка не найдена")
    else:
        print(f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {str_shelfs()}.")


def add_document_to_directory():
    """
    Prompt the user to input document details and add the document to the directory if the specified shelf exists.

    :return: None
    """
    doc_number = input("Введите номер документа: ").strip()
    doc_type = input("Введите тип документа: ").strip()
    doc_own = input("Введите владельца документа: ").strip()
    shelf = input("Введите полку: ").strip()

    if shelf not in directories:
        all_info_about_docs()
        print(f"Такой полки не существует. Добавьте полку командой as.")
        print(f"Текущий список документов:")
        all_info_about_docs()
        return

    documents.append({'type': doc_type, 'number': doc_number, 'name': doc_own})
    directories[shelf].append(doc_number)
    print(f"Документ добавлен. Текущий список документов:")
    all_info_about_docs()


def delete_document(number):
    """
    :param number: The document number to be deleted.
    :return: None
    """
    removed_from_directories = False
    for shelf, docs in directories.items():
        if str(number) in docs:
            docs.remove(str(number))
            removed_from_directories = True

    removed_from_documents = False
    for doc in documents:
        if doc['number'] == str(number):
            documents.remove(doc)
            removed_from_documents = True
            break

    if removed_from_directories and removed_from_documents:
        print(f"Документ удален.\nТекущий список документов:")
        all_info_about_docs()
    else:
        print("Документ не найден в базе:")
        print(f"Текущий список документов:")

        all_info_about_docs()

def move_document(number, shelf):
    """
    :param number: The document number to be moved.
    :param shelf: The shelf number to which the document will be moved.
    :return: None
    """

    if str(shelf) not in directories:
        print("Такой полки не существует")
        print(f"Текущий перечень полок: {str_shelfs()}.")

    elif document_shelf(number) == "Документ не найден в базе":
        print("Документ не найден в базе.\nТекущий список документов:")
        all_info_about_docs()

    elif str(number) in directories[str(shelf)]:
        print("Документ уже находится на этой полке")

    else:
        for shelf_docs in directories.values():
            if str(number) in shelf_docs:
                shelf_docs.remove(str(number))
                break
        directories[str(shelf)].append(str(number))
        print(f"Документ перемещен на полку {shelf}.\nТекущий список документов:")
        all_info_about_docs()


# move_document("11-2",3)


def main():
    while True:
        command = input("Введите команду: ").lower().strip()
        if command == 'q':
            break
        elif command == 'p':
            number = input("Введите номер документа: ").strip()
            print(doc_owner(number))
        elif command == 's':
            number = input("Введите номер документа: ").strip()
            print(document_shelf(number))
        elif command == 'l':
            all_info_about_docs()
        elif command == 'ads':
            number = input("Введите номер полки: ").strip()
            add_shelf(number)
        elif command == 'ds':
            number = input("Введите номер полки: ").strip()
            delete_shelf(number)
        elif command == 'ad':
            add_document_to_directory()
        elif command == 'd':
            number = input("Введите номер документа: ").strip()
            delete_document(number)
        elif command == 'm':
            number = input("Введите номер документа: ").strip()
            shelf = input("Введите полку: ").strip()
            move_document(number, shelf)

main()
