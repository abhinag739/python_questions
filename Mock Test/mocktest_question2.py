# The list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to hold the result
    current = dummy  # Pointer to iterate through the result linked list
    carry = 0  # Variable to track the carry
    
    while l1 or l2 or carry:
        # Calculate the sum of current digits and the carry
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = sum // 10  # Update the carry
        digit = sum % 10  # Calculate the current digit
        
        # Create a new node for the current digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to the next nodes in the input linked lists, if available
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next  # Return the result linked list starting from the next node of the dummy

# Example usage:
# Constructing the input linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)

# Print the result linked list
while result:
    print(result.val, end=" ")
    result = result.next

# Output: 7 0 8
