import os


class DirectoryBrowser:

    def __init__(self, dirname):
        self.dirname = dirname
        self.content = None

    def get_dir_contents(self):
        """
        Mетод создает атрибут класса в ввиде словаря
        {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
        :return:
        """
        directory = list()
        file = list()
        for item in os.listdir(self.dirname):
            if os.path.isdir(item):
                directory.append(item)
            else:
                file.append(item)
        self.content = {'filenames': file, 'dirnames': directory}
        return self.content

    def directory_sorting(self, reverse):
        """
        Mетод получает булевое значение (True/False).
        Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
        Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
        :param reverse:
        :return:
        """
        if isinstance(reverse, bool):
            self.content['filenames'].sort(reverse=reverse)
            self.content['dirnames'].sort(reverse=reverse)
            return self.content
        else:
            print('Input False or True')

    def add_dir_element(self, element):
        """
        Mетод класса получает строку, которая может быть
        или именем файла, или именем папки.
        В зависимости от того, что метод получил(имя файла или имя папки) - записывает его
        в соответствующий список и веращает обновленный словарь.
        :param element:
        :return:
        """
        if '.' in element[1:]:
            self.content['filenames'].append(element)
        else:
            self.content['dirnames'].append(element)
        print(self.content)

    def get_new_elements(self, new_content):
        """
        Метод класса получает словарь.
        Метод проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
        если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
        :param new_content:
        :return:
        """
        for item in new_content['dirnames']:
            if not item in self.content['dirnames']:
                os.mkdir(item)
        for item in new_content['filenames']:
            if not item in self.content['filenames']:
                open(item, "w")


path_to_elements = os.path.join(input('Enter the directory name: '))
directory = DirectoryBrowser(path_to_elements)
print(directory.get_dir_contents())
directory.add_dir_element('Dir555')
directory.add_dir_element('File555.txt')
print(directory.directory_sorting(False))
directory.get_new_elements(new_content={'filenames': ['file5.txt', 'file6.txt'], 'dirnames': ['Dir5', 'dir6']})
