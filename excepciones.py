s = raw_input("enter an integer: ")

try:
    i = int(s)
    print ('valid integer,entered', i)
except ValueError as err:
    print ('error', err)
#except NameError as err:
#    print ('es una letra')
finally:
    print ('finally')


total = 0
count = 0
#%s es para strings
#%d es para integer o decimales
while True:
    line =raw_input('integer: ')
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print (err)
            continue
        total +=number
        count += 1
    else:
        break

if count:
    print 'count = %d total = %d mean = %d'%(count, total, total/count)

