yes    ='y'
emptyty   =0
kilkist_and=0
kilkist_z  =0
sum_z =0
while yes=='y':
  print('do you want more?(y/n)')
  yes = input()
  if yes=='y':
     print('text filename:')#"text.txt"
     name = input()
     f1 = open(name,"r")
     print(name)
     lines = f1.readlines()
     print(lines)
     numstr = len(lines)
     for stri in lines:
         print(stri)
         if len(stri)==1:
            emptyty=emptyty+1
         else:#z
             ind = stri.count('z')
             kilkist_z = kilkist_z + ind
             if ind>0:
                sum_z = sum_z + 1#and
             ind = stri.count('and')
             kilkist_and = kilkist_and + ind 
     print('strings: ',numstr)
     print('  emptytyty: ',emptyty)
     print(' with z: ',sum_z)
     print('      z: ',kilkist_z)
     print('    and: ',kilkist_and)
     f1.close()

