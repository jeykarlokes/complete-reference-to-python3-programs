# fruits = "{},{},{},{},{}"
# print(fruits.format(1,2,3,4,6))
# print(fruits.format("1","2","3","4","5"))
# print(fruits.format("orange","mango","grapes","lemon","banana"))
# print(fruits.format(True,False,True , False,True))
# print(fruits.format("orange  is super \n","BANANA IS FAVORITE FOR MONKEYS \n","mango is very sweet\n","grapes is sour \n","lemon is salt and crimy taste"))

#we can also get input using argv
# from sys import argv
# first,second,third = argv
# # the first will be printed as the name of the file
# print(f"{first} is the winner")
# print(f"{second} is the runner")
# print(f"{third} is the looser")

# from sys import argv
# script,file_name = argv
# hello = input("your file will ber opened soon !")
# text = open(file_name)
# red = input("do you want to read it ")
# print(text.read())
# red = input("do you want to read it one more ")
# file_again = input("> enter ur file name :")
# text_new = open(file_again)
# print("here's your file")
# print(text_new.read())

# from sys import argv
# script,file_name = argv
# print(f"we ar going to erase{file_name}")
# print("if you don't want that , hit CTRL-C.")
# print("if you do want that , hit RETURN")
# input("?")
# print("opening the fie......")
# target = open(file_name,"w")
# # print("Truncating the file,goodbye ")
# # target.truncate()
# print("now I'm going to ask u three lines ")
# line1 = input("line 1 :")
# line2 = input("line 2 :")
# line3 = input("line 3 :")
# print("I'm going to write these to the fie")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# print("AND finally , we close it ..")
# target.close()

from sys import argv
from os.path import exists
script,fromfile,tofile = argv
print(f"we r going to copy from {fromfile} to {tofile}")
fromfile = open(fromfile)
fromfiles = fromfile.read()
print(f"check the whether {tofile} exisits ?")
tofile = open(tofile,"w")
to_data = tofile.write(fromfiles)
print("the copiedd data is ::::::")
# print(tofile.read())
fromfile.close()
tofile.close()
















# from os.path import exists
# script,from_file,to_file = argv
# print(f"copying from {from_file} to {to_file}")
# in_file =open(from_file)
# indata = in_file.read()
# print(f"the input file is {len(indata)} bytes long")
# print(f"Does the output file exists? {exists(to_file)}")
# input()
# out_file = open(to_file,"w")
# out_file.write(indata)
# print("ALright , all done , ")
# out_file.close()
# in_file.close()





