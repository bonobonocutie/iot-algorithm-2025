# 재귀호출 테스트

def factorial(n):
    if n <= 1:
        print('1 반환')
        return 1
    print(f'{n} * {n-1}! 호출')
    retVal = factorial(n-1)

    print(f'{n} * {n-1} 반환 (={retVal})' )
    return n * retVal

print(f'\n5! = {factorial(5)}')