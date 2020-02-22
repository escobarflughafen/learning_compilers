import functools
import itertools


def append_all(list1, list2):
    if isinstance(list1, list):
        if isinstance(list2, list):
            l = []
            for i in list1:
                l.append(i)
            for i in list2:
                l.append(i)
            return l
        else:
            l = []
            for i in list1:
                l.append(i)
            l.append(list2)
            return l
    else:
        return append_all(list2, list1)


class NFA:

    def __init__(self, alphabet: list, trans_table: list):
        self.alphabet = alphabet
        self.trans_table = trans_table

    def epsilon_closure(self, s):
        try:
            stack = list(set(append_all([], self.trans_table[s][0])))
        except (KeyError, IndexError):
            stack = []
        
        closure = append_all([], stack)
        
        while len(stack) > 0:
            t = stack.pop()
            try:
                eps = append_all([], self.trans_table[t][0])
            except (KeyError, IndexError):
                eps = []
            for i in eps:
                if i not in stack:
                    stack.append(i)
                    closure.append(i)

        return list(set(append_all(s, closure)))
    
    def move(self, T: list, a):
        if (len(T) == 0):
            return []
        else:
            m = []
            for i in T:
                try:
                    m = append_all(m, self.trans_table[i][a])
                except (KeyError, IndexError):
                    pass
        return list(set(m))

    def epsilon_closure_T(self, T):
        closure = []
        for i in T:
            closure = append_all(closure, self.epsilon_closure(i))

        return list(set(closure))
            
    def D_tran(self, T: list, a):
        return self.epsilon_closure_T(self.move(T, a))

                # epsilon -- 0
nfa1 = NFA(['a', 'b'], [{0: [1, 7]}, {0: [2, 4]}, {'a': [3]}, {0: [6]}, {
           'b': [5]}, {0: [6]}, {0: [1, 7]}, {'a': [8]}, {'b': [9]}, {'b': [10]}, {}])

print(nfa1.D_tran(nfa1.epsilon_closure(0), 'a'))
print(nfa1.D_tran(nfa1.epsilon_closure(0), 'b'))