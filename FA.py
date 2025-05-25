'''
Parameters is mean:
q -> a set of state
Sigma -> a set of input symbols
q0 -> a state in q, it is the initial state
F -> a set of state in q, and they mean's the final state

the delta is a dictionary like:
{
    q0: {
        symbol1: q1,
        symbol2: q2
    },
    q1: {
        symbol1: q2,
        symbol2: q3
    }
}
It simulate to a transfer table.using by simulate the transfer function.
you must define all possible transfer.
'''
class dfa:
    def __init__(self, q:set, Sigma:set, delta:dict, q0, F:set):
        self.q:set = q
        self.Sigma:set = Sigma
        self.delta:dict = delta
        self.q0 = q0
        self.F:set = F
    def run(self, input: list) -> bool:
        state = self.q0
        for symbol in input:
            state = self.delta[state][symbol]
        if state in self.F:
            return True
        else:
            return False
