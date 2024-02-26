import argparse
from colorama import Fore,Back,Style,init
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
        nargs="+" 
        )
parser.add_argument(
        "-s" "--sub",
        help="subtraction any number",
        metavar="subtraction operation",
        dest="sub",
        nargs="+" ,
            
        )
parser.add_argument(
        "-d" "--div",
        help="divide any number",
        metavar="divide operation",
        dest="div",
        nargs="+" ,
            
            
        )
parser.add_argument(
        "-m" "--multi",
        help="multiplay any number",
        metavar="multiplay operation",
        dest="multi",
        nargs="+" ,
            
        )

args=parser.parse_args()
add=args.add
#print(add)
sub=args.sub
#print(sub)
div=args.div
#print(div)
multi=args.multi
#print(multi)

if add: 
    result=0
    for i in add: 
        integer=int(i)       
        result+=integer
    print(Fore.LIGHTYELLOW_EX+"Total :",result)

elif sub:    
    result=int(sub[0])
    for i in sub[1:]: 
        integer=int(i)       
        result= result-integer
        
    print(Fore.BLUE+"Total :",result)


elif div:    
    result=int(div[0])
    for i in div[1:]: 
        integer=int(i)       
        result= result / integer
        
    print(Fore.CYAN+"Total :",result)
    
elif multi:    
    result=1
    for i in multi: 
        integer=int(i)       
        result= result*integer
        
    print(Fore.GREEN+"Total :",result)
