tuple=immutable_var='Husky',2,[1,2,3],True,3.5
print(str('Immutable tuple: ')+str(tuple))

mutable_list=['Husky',2,[1,2,3],True,3.5]
mutable_list[0]='Cat'
print(str('Mutable list: ')+str(mutable_list))


tuple[0]=8
print(tuple)