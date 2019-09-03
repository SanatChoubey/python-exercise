try:
     Age = int(input("Age :"))
except ValueError:
     print('error')  
finally:
     print('i am done')        