#!/usr/bin/env python3

def mysort(dat, start, end):
    pass
    #---------------------- 
    # write your code here
    #---------------------- 

#---------------------------------------------------------------------
# you can modify the following to test your code more thoroughly
#---------------------------------------------------------------------
data = ['18 64 54 4 36 55 28 10 82 94 59 78 88 18 37 39 75', 
        '34 21 83 94 20 95 7 73 95 17 100 16 56 46 33 66 31 31 100 63', 
        '43 41 97 76 15 42 18 67 9 30 44 13 5 10 4 90 53 19 44 17 36 35', 
        '77 8 54 32 37 7 60 0', 
        '7 13 70 60 12 32 71 38 68 18 37 98 38 44 31 87 44 13 89', 
        '51 78 49 51 35 99 54 83 43 100 58 25 61 85 43 33 11 12 18 8 100 12 44 84', 
        '53 50 44 73 18 56 16 21 29 62 15 78 10 82 55 7 6 19 10 21 15', 
        '53 33 49 91 32 22 84 45 31 79 22 44 93 19', 
        '32 44 9 37 81 5 95 24 49 55 46 18 13 15 31 65 78 39 38 42 1 54 68 80 94', 
        '100 44 40 92 29 99 17 2 27 96 23 26 48 65 77 23 17 17 83'
        ]

def main():
    global data
    for test_case in data:
        result = mysort(test_case,5,15);
        print(result)
        
if __name__ == '__main__':
    main()