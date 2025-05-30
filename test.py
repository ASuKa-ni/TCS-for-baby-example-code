import FA

testDFA = FA.dfa(
    q = {'q0', 'q1'},
    Sigma = {'0', '1'},
    delta = {
    ('q0',0): 'q0',
    ('q0',1): 'q1',
    ('q1',0): 'q1',
    ('q1',1): 'q0'
    },
    q0 = 'q0',
    F = {'q1'}
)

print(testDFA.run([1,0,1,0,1]))