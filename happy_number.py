def numSum(n):
    squareSum = 0;
    while(n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;

def Happynum(n):

    s = n;
    f = n;
    while(True):
        slow = numSum(s);
        fast = numSum(numSum(f));
        if(slow != fast):
            continue;
        else:
            break;
    return (s == 1);

n = 13;
if (Happynum(n)):
    print(n , "is a Happy number");
else:
    print(n , "is not a Happy number");
