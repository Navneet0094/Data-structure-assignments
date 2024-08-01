class BrowserHistory:

    class PageNode:
        def __init__(self, url):
            self.url = url
            self.prev = None
            self.next = None
    def __init__(self, homepage:str):
        self.curr = self.PageNode(homepage)

    def visit(self, url:str) -> None:
        newpage = self.PageNode(url)
        newpage.prev = self.curr
        self.curr.next = newpage
        self.curr = newpage

    def back(self, steps:int)-> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps:int)-> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url