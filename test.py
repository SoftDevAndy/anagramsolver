# Andrew Sweeney
# G00237144
# February 2016

# Test Functions

import solver


def test_checkvalidconundrum():
    print('\ntest_checkvalidconundrum\n')
    print(solver.checkvalidconundrum('AAAAAAAAAA'))
    print(solver.checkvalidconundrum('BBBBBBBBBB'))
    print(solver.checkvalidconundrum('123456789'))
    print(solver.checkvalidconundrum('testing'))
    print(solver.checkvalidconundrum('conundrum'))
    print(solver.checkvalidconundrum('AAABBBBBB'))
    print(solver.checkvalidconundrum('CONUNDRUM'))

# Run test functions

test_checkvalidconundrum()
