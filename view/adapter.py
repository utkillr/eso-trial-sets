class ViewAdapter:

    def __init__(self, s: str, limit: int = 1950):
        self.s = s
        self.limit = limit

    def _cut_by(self, sub, start=0, prefix='', suffix=''):
        if self.limit + start >= len(self.s):
            res = self.s
            self.s = ''
            return res
        position = self.s[start:self.limit + len(sub) + start].rfind(sub)

        if position != -1:
            position += start
            res, self.s = self.s[:position] + suffix, prefix + self.s[position + len(sub):]
            return res
        else:
            raise StopIteration(f'No "{sub}" in first {self.limit} chars starting from index {start}')

    def cut(self, first: bool):
        start = 0 if first else 4
        # two breaks
        try:
            return self._cut_by('\n\n', prefix='...\n', start=start)
        except StopIteration:
            pass
        # one break
        try:
            return self._cut_by('\n', prefix='...\n', start=start)
        except StopIteration:
            pass
        # space
        try:
            return self._cut_by(' ', prefix='...', suffix='...', start=start)
        except StopIteration:
            pass
        # cut
        res, self.s = self.s[:self.limit + start] + '...', '...' + self.s[self.limit + start:]
        return res

    def adapt(self):
        # return [self.s]

        if len(self.s) <= self.limit:
            return [self.s]

        res = []

        first = True
        while len(self.s) > self.limit:
            cut = self.cut(first)
            res.append(cut)
            first = False
        if self.s:
            res.append(self.s)
        return res


