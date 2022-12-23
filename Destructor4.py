class Foo():
    def __init__(self, id, bar):
        self.id = id;
        # saving reference of Bar object
        self.friend = bar;
        print ('Foo', self.id, 'born');

    def __del__(self):
        (print 'Foo', self.id, 'died');


class Bar():
    def __init__(self, id):
        self.id = id;
        self.friend = Foo(id, self);
        print ('Bar', self.id, 'born')

    def __del__(self):
        print ('Bar', self.id, 'died')


b = Bar(12)