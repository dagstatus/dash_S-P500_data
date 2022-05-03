class BaseFunc:
    @staticmethod
    def make_list_to_dropdown(list_in):
        dropdown_list = []
        for element in list_in:
            dropdown_list.append({'label': element, 'value': element})
        return dropdown_list
