def code_helper_tool(query: str) -> str:
    query_lower = query.lower()

    if "binary search" in query_lower:
        return """
Binary Search Template:

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

Time Complexity: O(log n)
"""

    if "java" in query_lower:
        return """
Java coding tip:
Use classes, clear method signatures, proper imports, and handle edge cases.
For DSA interviews, always explain time and space complexity.
"""

    if "python" in query_lower:
        return """
Python coding tip:
Use functions, type hints, clean error handling, and avoid unsafe eval.
"""

    return """
Coding helper:
Break the problem into input, logic, edge cases, complexity, and clean implementation.
"""