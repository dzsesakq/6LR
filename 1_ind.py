#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    def sort1(arr):
        result = arr[:3]
        result.sort(reverse=True)
        for i in arr[3:]:
            if i > result[-1]:
                result.pop()
                result.append(i)
                result.sort(reverse=True)
        return(result)
    
    athletes = []
    n = 0
    
    while n < 3:
        print(f'Введите количество спортсменов, но больше трех.')
        n = int(input())
        
    for i in range(n):
        ff = input(f'Введите фамилию спортсмена № {i + 1} ')
        print(f'Введите результаты прыжков спортсмена {ff} через пробел')
        athletes.append([max(list(map(int, input().split()))), ff])
    
    athletes = sort1(athletes)
    print(f'Первое место спортсмен {athletes[0][1]} с результатом {athletes[0][0]} метров\nВторое место спортсмен {athletes[1][1]} с результатом {athletes[1][0]} метров\nТретье место спортсмен {athletes[2][1]} с результатом {athletes[2][0]} метров')
