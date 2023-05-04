from typing import List


def max_equal_gap_seq(a: List[int]):
    """
    :param a: A list of positive integers of length greater than one.
    :return: The longest possible ordered sequence with the same "gap" between all elements.

    For example: [1,3,4,4,4,5] Should return [4,4,4] since these three elements all have a gap of 0.
    Other examples:
        [0,1,2,3,5,7] returns [1,3,5,7] (gap equals 2)
        [0,10,20,50] returns [0,10,20] (gap equals 10)

    """
    a.sort()  # Easier (obligatory?) for processing
    gap_sizes = range(0, max(a) + 1)  # Need to add one since range does not include the upper bound. Consider [0,0,0,0]

    overall_max_sequence = []  # Keep track of the overall longest sequence across all gap sizes

    for gap_size in gap_sizes:
        previous = None  # Prepare the previous value. It's None for the first element in the list
        max_sequence = []  # The maximum sequence for a given gap
        current_sequence = []  # Keep track of the current sequence
        for current in a:

            if previous is not None:
                # If current sequence is empty, insert current element
                if len(current_sequence) == 0:
                    current_sequence.append(previous)

                # Now we have current and previous. Compare and see if their diff equals the desired gap size
                actual_gap_size = current - previous

                if actual_gap_size == gap_size:
                    # Append the current sequence with current element
                    current_sequence.append(current)

                    # Update the gap-specific maximum sequence if possible
                    if len(current_sequence) > len(max_sequence):
                        max_sequence = current_sequence
                else:
                    # Sequence has been broken (for now)! Reset the current sequence to only be current element
                    current_sequence = [current]  # Reset the sequence

            # Update previous
            previous = current

        # Now we have a gap-specific max sequence; check if it's longer than the current overall longest and replace
        # if needed
        if len(max_sequence) > len(overall_max_sequence):
            overall_max_sequence = max_sequence

    print(overall_max_sequence)
    # Finally, return the overall maximum sequence among all possible gaps
    return overall_max_sequence

