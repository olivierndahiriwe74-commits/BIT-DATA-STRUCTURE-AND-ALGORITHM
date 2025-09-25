from collections import deque

# -----------------------------
# STACK (LIFO)
# -----------------------------
print("=== STACK EXAMPLES ===")

# Example 1: MoMo steps
stack = [] 
stack.extend(["Dial Code", "Enter PIN", "Confirm"])  # push steps
print("MoMo stack:", stack)
stack.pop()  # undo once
print("After undo, top step is:", stack[-1])  # Enter PIN

# Example 2: UR assignments
stack = []
stack.extend(["AssignmentA", "AssignmentB", "AssignmentC"])
print("\nUR stack:", stack)
stack.pop()  # remove AssignmentC
stack.pop()  # remove AssignmentB
print("Remaining assignment:", stack[-1])  # AssignmentA

# Example 3: Reverse string using stack
word = "QUEUEFAIR"
stack = list(word)  # push each letter
reversed_word = "".join([stack.pop() for _ in range(len(stack))])
print("\nOriginal word:", word)
print("Reversed word:", reversed_word)

# -----------------------------
# QUEUE (FIFO)
# -----------------------------
print("\n=== QUEUE EXAMPLES ===")

# Example 1: BK ATM with 7 clients
queue = deque(["C1", "C2", "C3", "C4", "C5", "C6", "C7"])
print("ATM queue:", list(queue))
for _ in range(3):  # serve first 3
    queue.popleft()
print("Client now in front:", queue[0])  # C4

# Example 2: RRA with 5 citizens
queue = deque(["P1", "P2", "P3", "P4", "P5"])
print("\nRRA queue:", list(queue))
queue.popleft()  # first served
print("Second served:", queue[0])  # P2
