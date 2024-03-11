def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # 遍历数组从0到n-i-1
            # 交换如果找到元素大于下一个元素
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试冒泡排序函数
sample_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(sample_array)
print("Sorted array is:", sorted_array)
