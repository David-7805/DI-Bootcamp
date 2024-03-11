from math import ceil

class Pagination:
    def __init__(self, items = None, page_size = 10):
        self.items = items
        self.page_size = round(page_size)
        self.current_page = 1

    def total_pages(self):
        return ceil(len(self.items) / self.page_size) # rounds to the nearest higher integer

    def pagination(self):
        dict_of_pages = {}
        total_pages = self.total_pages()
        for page in range(1, total_pages + 1):
            dict_of_pages[page] = self.items[((page - 1) * self.page_size): (page * self.page_size)]
        return dict_of_pages

    def get_visible_items(self):
        return self.pagination()[self.current_page]

    def prev_page(self):
        self.current_page -= 1
        self.to_closest_existing_page()
        return self

    def next_page(self):
        self.current_page += 1
        self.to_closest_existing_page()
        return self

    def first_page(self):
        self.current_page = 1

    def last_page(self):
        self.current_page = self.total_pages()

    def go_to_page(self, page_number):
        self.current_page = round(page_number)
        self.to_closest_existing_page()

    def to_closest_existing_page(self):
        if self.current_page < 1:
            self.current_page = 1
        elif self.current_page > self.total_pages():
            self.current_page = self.total_pages()


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.total_pages())
print(p.get_visible_items())
p.next_page().next_page()
print(p.get_visible_items())
p.prev_page().prev_page()
print(p.get_visible_items())
p.first_page()
print(p.get_visible_items())
p.last_page()
print(p.get_visible_items())
for i in range(0, p.total_pages() + 2): # includes also 2 non-existing pages
    p.go_to_page(i)
    print(p.get_visible_items())






