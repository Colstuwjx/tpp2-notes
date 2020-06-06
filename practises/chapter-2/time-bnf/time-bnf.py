# coding=utf-8

import bnfparsing


# caution:
# `hour := digit digit | digit` would broken
# if change it to `hour := digit | digit digit`.
TIMEBNF_STMT = """
time := hour ampm | hour ":" minute ampm | hour ":" minute
ampm := "am" | "pm"
hour := digit digit | digit
minute := digit digit
digit := "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"
"""


class TimeBNFStmtParser(bnfparsing.ParserBase):
    def __init__(self):
        super().__init__(ws_handler=bnfparsing.ignore)
        self.grammar(TIMEBNF_STMT)

    def calc(self, parsed_node):
        result = 0
        for n in parsed_node.children:
            if n.token_type == 'ampm' and n.value() == 'am':
                result += self._am()
            elif n.token_type == 'ampm' and n.value() == 'pm':
                result += self._pm()
            elif n.token_type == 'hour':
                result += self._h(n.value())
            elif n.token_type == 'minute':
                result += self._m(n.value())
            elif n.token_type == 'literal':
                pass
            else:
                raise Exception('Unknown token {}'.format(n.token_type))
        return result

    def _h(self, h):
        return int(h)*60

    def _m(self, m):
        return int(m)

    def _am(self):
        return 0

    def _pm(self):
        return 12*60


if __name__ == '__main__':
    p = TimeBNFStmtParser()

    t_pm4 = p.calc(p.parse("4pm"))
    t_pm738 = p.calc(p.parse("7:38pm"))
    t_2342 = p.calc(p.parse("23:42"))
    t_316 = p.calc(p.parse("3:16"))
    t_am316 = p.calc(p.parse("3:16am"))

    print("results: {}, {}, {}, {}, {}".format(
        t_pm4, t_pm738, t_2342, t_316, t_am316
    ))
