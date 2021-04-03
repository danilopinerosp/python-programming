#!/usr/bin/env python3

def runner_up(n):
    """ Return the runner-up score"""
    n = list(n)
    n.sort(reverse=True)
    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            return n[i]
    return n[0]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(runner_up(arr))
