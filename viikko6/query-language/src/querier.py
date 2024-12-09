from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

#Ex 4 & 5
class QueryBuilder:
    def __init__(self, stack = All()):
        self.stack = stack

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.stack, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.stack, HasFewerThan(value, attr)))
    
    def plays_in(self, team):
        return QueryBuilder(And(self.stack, PlaysIn(team)))
    
    def one_of(self, *matchers):
        return QueryBuilder(And(self.stack, Or(*matchers)))

    def build(self):
        return self.stack