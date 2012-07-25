#pprint1.py
#example of semi-useful functions

def Toporbottom(character,width):
    # width is total width of returned line
    return '%s%s%s' % ('+',(character*(width-2)),'+')

def Fmt(val1,leftbit,val2,rightbit):
    part2='%.2f' %val2
    return '%s%s%s%s' % ('| ',val1.ljust(leftbit-2,' '),part2.rjust(rightbit-2,' '),' |')

# define the price of each item
item1=3.00
item2=15.00
#now print evething out......
print Toporbottom('=',40)
print Fmt('item1',30,item1,10)
print Fmt('item2',30,item2,10)
print Toporbottom('-',40)
print Fmt('total',30,item1+item2,10)
print Toporbottom('=',40)
