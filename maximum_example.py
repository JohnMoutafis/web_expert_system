from pyknow import *


class Maximum(KnowledgeEngine):
    """
    Implements pyknow example of calculating maximum of list.
    """
    @Rule(~Fact(max=W()))
    def init(self):
        self.declare(Fact(max=0))

    @Rule(
        Fact(val='val' << W()),
        'm' << Fact(max='max' << W()),
        TEST(lambda max, val: val > max)
    )
    def compute_max(self, m, val, max):
        self.modify(m, max=val)

    @Rule(
        'v' << Fact(val=W('val')),
        Fact(max=W('max')),
        TEST(lambda max, val: val <= max)
    )
    def remove_val(self, v, max, val):
        self.retract(v)

    @Rule('v' << Fact(max=W()) & ~Fact(val=W()))
    def print_max(self, v):
        self.response = v['max']


compute_max = Maximum()
