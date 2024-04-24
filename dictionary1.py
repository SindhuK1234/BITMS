'''def sindhu():
    return 'This is my bank balance'
test_dict={'fname':sindhu,'age':20,'address':'ballari'}#fname is function name
print('The original dict is:'+str(test_dict))
res=test_dict['fname'](10,20)
print('The required call result:'+str(res))'''
def sindhu(a,b):
    return ('This is my bank balance',a+b)
test_dict={'fname':sindhu,'age':20,'address':'ballari'}#fname is function name
print('The original dict is:'+str(test_dict))
res=test_dict['fname'](10,20)
print('The required call result:'+str(res))