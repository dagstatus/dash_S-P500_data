class BaseFunc:
    @staticmethod
    def make_list_to_dropdown(label_list_in, value_list_in):
        dropdown_list = []
        for label_el, value_el in zip(label_list_in, value_list_in):
            dropdown_list.append({'label': label_el, 'value': value_el})
        return dropdown_list
