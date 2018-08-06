# -*- coding: utf-8 -*-
# define functions for sort algorithm
# By yanxing

# 插入排序
def insertsort(x):
    for i in range(len(x)):
        startx = 0;
        endx = i;
        while startx < endx:
            j = (startx + endx) // 2
            if x[i] > x[j]:
                endx = j
            else:
                startx = j + 1
        y = x[i]
        for t in range(i, startx, -1):
            x[t] = x[t - 1]
        x[startx] = y
    return


# 冒泡排序
def bublesort(x):
    for i in range(len(x)):
        for j in range(0, len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return


# 选择排序
def selectsort(x):
    for i in range(len(x)):
        t0 = i
        t1 = x[i]
        for j in range(i + 1, len(x)):
            if x[j] < t1:
                t1 = x[j]
                t0 = j
        if t0 != i:
            x[t0] = x[i]
            x[i] = t1
    return


# 堆排序
def heapsort(x):
    if len(x) <= 0:
        return
    # 建立大根堆
    buildheap(x)
    # 建立大根堆完成
    heaplen = len(x)
    while 1:
        # 提出根结点
        x[0], x[heaplen - 1] = x[heaplen - 1], x[0]
        # print(heaplen,':',x)
        heaplen -= 1
        if heaplen == 0:
            break
        # 将新的根结点放到合适的位置
        cnode = 0
        while 1:
            snode1 = (cnode + 1) * 2
            snode2 = snode1 - 1
            node = cnode
            maxv = x[cnode]
            if snode1 < heaplen:
                if maxv < x[snode1]:
                    maxv = x[snode1]
                    node = snode1
            if snode2 < heaplen:
                if maxv < x[snode2]:
                    maxv = x[snode2]
                    node = snode2
            # 如果没有交换，就可以退出了
            if node == cnode:
                break
            x[node] = x[cnode]
            x[cnode] = maxv
            cnode = node
    return


# 建立堆，ptype=1,为大根堆，ptype=2为小根堆
def buildheap(x, ptype=1):
    heaplen = len(x)
    for i in range(heaplen // 2, -1, -1):
        if ptype == 1:
            cnode = i
            while 1:
                snode1 = (cnode + 1) * 2
                snode2 = snode1 - 1
                node = cnode
                maxv = x[cnode]
                if snode1 < heaplen:
                    if maxv < x[snode1]:
                        maxv = x[snode1]
                        node = snode1
                if snode2 < heaplen:
                    if maxv < x[snode2]:
                        maxv = x[snode2]
                        node = snode2
                # 如果没有交换，就可以退出了
                if node == cnode:
                    break
                x[node] = x[cnode]
                x[cnode] = maxv
                cnode = node
        else:
            cnode = i
            while 1:
                snode1 = (cnode + 1) * 2
                snode2 = snode1 - 1
                node = cnode
                maxv = x[cnode]
                if snode1 < heaplen:
                    if maxv < x[snode1]:
                        maxv = x[snode1]
                        node = snode1
                if snode2 < heaplen:
                    if maxv < x[snode2]:
                        maxv = x[snode2]
                        node = snode2
                if node == cnode:
                    break
                x[node] = x[cnode]
                x[cnode] = maxv
                cnode = node
    return


# 快速排序, 非递归方式
def quicksort2(x, start, end):
    stack = []
    node = [start, end]
    stack.append(node)
    # stacklen=1
    while len(stack) > 0:
        # if (len(stack)>stacklen):
        #    stacklen=len(stack)
        node = stack.pop()
        start = node[0]
        end = node[1]
        if start >= end:
            continue
        key = x[start]
        i = start
        j = end
        while (i < j):
            while (i < j) & (key < x[j]):
                j -= 1
            x[i] = x[j]
            while (i < j) & (key >= x[i]):
                i += 1
            x[j] = x[i]
        x[i] = key
        node = [start, i - 1]
        stack.append(node)
        node = [i + 1, end]
        stack.append(node)
    # print(stacklen)
    return


# 快速排序, 递归方式
def quicksort(x, start, end):
    # print(start,end)
    if start >= end:
        return
    key = x[start]
    i = start
    j = end
    while (i < j):
        # print("1:i,j",i,j)
        while (i < j and key < x[j]):
            j -= 1
        x[i] = x[j]
        # print("2:i,j",i,j)
        while (i < j and key >= x[i]):
            i += 1
        x[j] = x[i]
    x[i] = key
    quicksort(x, start, i - 1)
    quicksort(x, i + 1, end)
    return


''' 希尔排序
x : 待排序的序列
incseq : 希尔排序增量的类型（缺省=1）：1-Hibbard, 2-Sedgewick, 3-Knuth, 4-Gonnet, 
'''
def shellsort(x,incseq=1):
    d = []
    if incseq == 1:
        IncrementSequenceBuild_Hibbard(len(x),d)
    elif incseq == 2:
        IncrementSequenceBuild_Sedgewick(len(x),d)
    elif incseq == 3:
        IncrementSequenceBuild_Knuth(len(x), d)
    elif incseq == 4:
        IncrementSequenceBuild_Gonnet(len(x), d)
    # print(d)
    if d[0] == 1:
        for i in range(len(d) - 1, 0, -1):
            shellpass(x, d[i])
    else:
        for i in range(1, len(d)):
            shellpass(x, d[i])
    return


def shellpass(x, d):
    xlen = len(x)
    i = 0
    while i < d:
        j = i + d
        # print(i)
        while j < xlen:
            key = x[j]
            t = j - d
            while t >= i:
                if x[t] >= key:
                    x[t + d] = x[t]
                    t -= d
                else:
                    break
            x[t + d] = key
            j += d
        i += 1
    return


# 希尔排序，塞奇威克增量
def IncrementSequenceBuild_Sedgewick(seqlen, d):
    i = 1
    j = 2
    t1 = 9 * (1 << i * 2) - 9 * (1 << i) + 1
    t2 = (1 << j * 2) - 3 * (1 << j) + 1
    d.append(1)
    while seqlen >= d[len(d) - 1] * 2:
        if t1 > t2:
            d.append(t1)
            i += 1
            t1 = 9 * (1 << i * 2) - 9 * (1 << i) + 1
        else:
            d.append(t2)
            j += 1
            t2 = (1 << j * 2) - 3 * (1 << j) + 1
    return


# 希尔排序，Hibbard增量
def IncrementSequenceBuild_Hibbard(seqlen, d):
    i = 1
    t1 = 1
    while seqlen >= t1 * 2:
        d.append(t1)
        t1 = t1 * 2 + 1
    return


# 希尔排序，Knuth增量
def IncrementSequenceBuild_Knuth(seqlen, d):
    i = 1
    t1 = 1
    while seqlen >= t1 * 2:
        d.append(t1)
        t1 = t1 * 3 + 1
    return


# 希尔排序，Gonnet增量
def IncrementSequenceBuild_Gonnet(seqlen, d):
    t1 = int(seqlen // 2.2)
    while t1 >= 1:
        if t1 == 2:
            d.append(2)
            d.append(1)
            break
        d.append(t1)
        t1 = int(t1 // 2.2)
    return

#归并排序
def mergesort(x):
    step = 1
    while step < len(x):
        left = 0
        right = 0
        while 1:
            left = right
            if left >= len(x):
                break
            mid = left + step
            if mid >= len(x):
                break
            right = mid + step
            if right > len(x):
                right = len(x)
            merge(x, left, mid, right)
        step = step << 1
    return


def merge(x, left, mid, right):
    i = left
    j = mid
    head = left
    y = []
    while head < mid:
        if x[i] <= x[j]:
            y.append(x[i])
            i += 1
            if i >= mid:
                while j < right:
                    y.append(x[j])
                    j += 1
                break
        else:
            y.append(x[j])
            j += 1
            if j >= right:
                while i < mid:
                    y.append(x[i])
                    i += 1
                break
    j = 0
    for i in range(left, right):
        x[i] = y[j]
        j += 1
    return
