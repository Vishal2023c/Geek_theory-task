import argparse
from colorama import Fore,Back,Style,init
def add(a,b):
    val = a+b
    return val

def sub(a,b):
    val = a-b
    return val

def div(a,b):
    val = a/b
    return val
 

def multi(a,b):
    val = a*b
    return val


def Main():
    parser= argparse.ArgumentParser(
            description="This is a calculator in which you can calculate numbers.",
            usage='%(prog)s -a -s -d -m' ,
            epilog="example : %(prog)s -a enter any number",           
        )
    parser.add_argument(
            "-a" "--add",
            help="Add any number",
            metavar="Add operation",
            dest="add",
            # nargs="+" 
            )
    parser.add_argument(
            "-s" "--sub",
            help="subtraction any number",
            metavar="subtraction operation",
            dest="sub",
            # nargs="+" ,
            
            )
    parser.add_argument(
            "-d" "--div",
            help="divide any number",
            metavar="divide operation",
            dest="div",
            # nargs="+" ,
            
            
            )
    parser.add_argument(
            "-m" "--multi",
            help="multiplay any number",
            metavar="multiplay operation",
            dest="multi",
            # nargs="+" ,
            
            )
    parser.add_argument("num1",help="Number1 to calculate",type=int)
    parser.add_argument("num2",help="Number2 to calculate",type=int)
 
# parser.add_argument(
#             "-md " "-modulus ",
#             help="modulus any number",
#             metavar="modulus operation",
#             dest="mod",
#             nargs="+" ,
            
#             )
    args=parser.parse_args()

    if args.add:
            print("The addition result of {} and {} is {}".format(args.add,args.add,(add(args.add,args.add))))
    elif args.sub:
            print("The subtraction result of {} and {} is {}".format(args.num1,args.num2,(sub(args.num1,args.num2))))
    elif args.div:
            print("The division result of {} and {} is {}".format(args.num1,args.num2,(div(args.num1,args.num2))))
    elif args.multi:
            print("The multiplication result of {} and {} is {}".format(args.num1,args.num2,(multi(args.num1,args.num2))))
    else:
            print("Error:Requires an argument to perform an action")
    
if __name__ == '__main__':
    Main()

# add=args.add
# print(add)
# sub=args.sub
# print(sub)
# div=args.div
# print(div)
# multi=args.multi
# print(multi)
# # mod=args.mod
# # print(mod)

# if add: 
#     result=0
#     for i in add: 
#         integer=int(i)       
#         result+=integer
#     print("Total :",result)

if sub:    
    result=0
    for i in sub: 
        print(i)
        integer=int(i)       
        result=result-integer
        
    print(Fore.LIGHTYELLOW_EX+"Total :",result)   

# elif div:    
#     result=0
#     for i in div: 
#         integer=int(i)       
#         result= integer
        
#     print("Total :",result) 
    
# elif multi:    
#     result=1
#     for i in multi: 
#         integer=int(i)       
#         result= result*integer
        
#     print("Total :",result)

# elif mod:    
#     result=0
#     for i in mod: 
#         integer=int(i)       
#         result= result%integer
#     print("Total :",result) 
