def merge_two_sorted_arrays(nums1, nums2):
    result = []
    n = len(nums1)
    m = len(nums2)
    i, j = 0, 0

    while i < n and j < m:
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < n:
        result.append(nums1[i])
        i += 1

    while j < m:
        result.append(nums2[j])
        j += 1

    print(result)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 5, 5, 5, 5, 6]
    nums2 = [2, 5, 6]
    merge_two_sorted_arrays(nums1, nums2)
