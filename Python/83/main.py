def deleteDuplicates(head):
    if not head:
        return head
    i = 0
    while i < len(head) - 1:
        if head[i] == head[i+1]:
            head.pop(i+1)
        else:
            i += 1
    return head
def bubbleSort(head):
    n = len(head)
    for i in range(n):
        rem = True
        for j in range(n-i-1):
            if head[j] > head[j+1]:
                head[j], head[j+1] = head[j+1], head[j]
                rem = False
        if rem:
            break
head = [1, 1, 1, 1, 2, 62, 62, 32, 32, 92, 2, 2, 3, 31, 31, 23, 23, 523, 23, 3, 3, 3, 3]
bubbleSort(head)
deleteDuplicates(head)
print(head)
