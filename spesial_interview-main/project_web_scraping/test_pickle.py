import pickle


sub_list1 = []
sub_list1.append(['4'])
sub_list1.append(['55', '55'])
sub_list1.append(['666', '666', '666'])

sub_list2 = []
sub_list2.append(['77', '77', '77'])
sub_list2.append(['88', '88', '88'])
sub_list2.append(['99', '99', '99'])

main_list = []
main_list.append(['1aaaa', '1bbbb', sub_list1])
main_list.append(['2aaaa', '2bbbb', sub_list2])


print()
print()

# print('len(main_list) : {}' .format(len(main_list)))
# print('len(main_list[0]) : {}' .format(len(main_list[0])))
# print('len(main_list[1]) : {}' .format(len(main_list[1])))
# print('len(main_list[0][0]) : {}' .format( len(main_list[0][0]) ))
# print('len(main_list[0][1]) : {}' .format( len(main_list[0][1]) ))
# print('len(main_list[0][2]) : {}' .format( len(main_list[0][2]) ))

# print('len(main_list[0][1][0]) : {}' .format( len(main_list[0][1][0]) ))
# print('len(main_list[0][1][1]) : {}' .format( len(main_list[0][1][1]) ))
# print('len(main_list[0][1][2]) : {}' .format( len(main_list[0][1][2]) ))

# print('len(main_list[0][2][0]) : {}' .format( len(main_list[0][2][0]) ))
# print('len(main_list[0][2][1]) : {}' .format( len(main_list[0][2][1]) ))
# print('len(main_list[0][2][2]) : {}' .format( len(main_list[0][2][2]) ))

# print(f'len(main_list) : {main_list}' )
# print()
# print(f'len(main_list[0]) : {main_list[0]}')
# print()
# print(f'len(main_list[1]) : {main_list[1]}' )
# print()
# print(f'len(main_list[0][0]) : {main_list[0][0]}' )
# print()
# print(f'len(main_list[0][1]) : {main_list[0][1]}' )
# print()
# print(f'len(main_list[0][2]) : {main_list[0][2]}' )
# print()

# print(f'len(main_list[0][1][0]) : {main_list[0][1][0]}' )
# print()
# print(f'len(main_list[0][1][1]) : {main_list[0][1][1]}' )
# print()
# print(f'len(main_list[0][1][2]) : {main_list[0][1][2]}' )
# print()

# print(f'len(main_list[0][2][0]) : {main_list[0][2][0]}' )
# print()
# print(f'len(main_list[0][2][1]) : {main_list[0][2][1]}' )
# print()
# print(f'len(main_list[0][2][2]) : {main_list[0][2][2]}' )
# print()


print()
print()

with open('./list.pickle', 'wb') as fw:
	pickle.dump(main_list, fw)
print('picle dump succ')

with open('./list.pickle', 'rb') as fr:
	read_list=pickle.load(fr)
print('picle load succ')



print(f'len(read_list) : {read_list}' )
print()
print(f'len(read_list[0]) : {read_list[0]}')
print()
print(f'len(read_list[1]) : {read_list[1]}' )
print()
print(f'len(read_list[0][0]) : {read_list[0][0]}' )
print()
print(f'len(read_list[0][1]) : {read_list[0][1]}' )
print()
print(f'len(read_list[0][2]) : {read_list[0][2]}' )
print()

print(f'len(read_list[0][1][0]) : {read_list[0][1][0]}' )
print()
print(f'len(read_list[0][1][1]) : {read_list[0][1][1]}' )
print()
print(f'len(read_list[0][1][2]) : {read_list[0][1][2]}' )
print()

print(f'len(read_list[0][2][0]) : {read_list[0][2][0]}' )
print()
print(f'len(read_list[0][2][1]) : {read_list[0][2][1]}' )
print()
print(f'len(read_list[0][2][2]) : {read_list[0][2][2]}' )
print()

