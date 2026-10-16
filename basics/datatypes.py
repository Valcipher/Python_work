####Numeric
#1. int
var=10

#2. float
var=3.14

#3. complex
var = 10 + 5j

#### text
#1.str
var = 'firstbit"sol"'
var = "first's sol"
var = '''
this is first line
this is second line'''

var = """
this is first line
this is second line"""

###sequential
#1.list
var = [10,20,30]

#2. tuple
var = (10,20,30)

#3. range
var = range(1,10)

print(type(var))
print(var)

###set type
#1.set
var = {10,20,30}

#2. frozenset
var = frozenset({10, 20, 30, 40})


####Mapping
#1. dict
var = {1:'python', 2:'java', 3:'c'}
print(type(var))

###other
#1. bool
var = True

#2. Nonetype
var= None
print(type(var))