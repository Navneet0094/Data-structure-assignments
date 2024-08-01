class StockSpanner:
    class Pair:
        def __init__(self, x, span):
            self.x = x
            self.span = span
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1].x <= price:
            p = self.stack.pop()
            span += p.span
        self.stack.append(self.Pair(price, span))
        return span