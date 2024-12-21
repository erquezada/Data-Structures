class NaturalMergeSorter:
    def __init__(self):
        return

    def get_sorted_run_length(self, integer_list, start_index):  
        if start_index < 0 or start_index >= len(integer_list):
            return 0

        run_length = 1
        current_index = start_index

        while current_index < len(integer_list) - 1 and integer_list[current_index] <= integer_list[current_index + 1]:
            run_length += 1
            current_index += 1

        return run_length

    def natural_merge_sort(self, integer_list):
        n = len(integer_list)

        while True:
            i = 0

            while i < n:
                # Get the length of the first sorted run starting at index i
                run1_length = self.get_sorted_run_length(integer_list, i)

                # If the first run's length equals the list's length, we are done
                if run1_length == n:
                    return

                # If the first run ends at the list's end, reassign i=0 and repeat
                if i + run1_length == n:
                    i = 0
                    continue

                # Get the length of the second sorted run starting immediately after the first
                run2_length = self.get_sorted_run_length(integer_list, i + run1_length)

                # Merge the two runs with the provided merge() method
                self.merge(integer_list, i, i + run1_length - 1, i + run1_length + run2_length - 1)

                # Reassign i with the first index after the second run, or 0 if the second run ends at the list's end
                if i + run1_length + run2_length == n:
                    i = 0
                else:
                    i = i + run1_length + run2_length

    def merge(self, numbers, left_first, left_last, right_last):
        merged_size = right_last - left_first + 1

        merged_numbers = [None] * merged_size
        merge_pos = 0
        left_pos = left_first
        right_pos = left_last + 1

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= left_last and right_pos <= right_last:
            if numbers[left_pos] <= numbers[right_pos]:
                merged_numbers[merge_pos] = numbers[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos] = numbers[right_pos]
                right_pos += 1

            merge_pos += 1

        # If left partition isn't empty, add remaining elements to merged_numbers
        while left_pos <= left_last:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
            merge_pos += 1

        # If right partition isn't empty, add remaining elements to merged_numbers
        while right_pos <= right_last:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
            merge_pos += 1

        # Copy merged numbers back to numbers
        for merge_pos in range(merged_size):
            numbers[left_first + merge_pos] = merged_numbers[merge_pos]
