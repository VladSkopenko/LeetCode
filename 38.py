class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"

        # Start with the initial sequence
        current_sequence = "1"

        for _ in range(2, n + 1):
            next_sequence = []
            count = 1

            # Iterate over the sequence to generate the next one
            for i in range(1, len(current_sequence)):
                if current_sequence[i] == current_sequence[i - 1]:
                    count += 1
                else:
                    next_sequence.append(str(count))
                    next_sequence.append(current_sequence[i - 1])
                    count = 1

            # Append the last group
            next_sequence.append(str(count))
            next_sequence.append(current_sequence[-1])

            # Update the sequence
            current_sequence = "".join(next_sequence)

        return current_sequence
