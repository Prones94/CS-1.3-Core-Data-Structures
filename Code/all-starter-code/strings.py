#!python
import re

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index = 0
    if len(pattern) == 0:
        return True
    for letter in text:
        if index > 0 and letter != pattern[index]:
             index = 0
        if letter == pattern[index]:
            index += 1
        if index > len(pattern) - 1:
            return True
    return False



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    pattern_index = 0
    pattern_found = 0

    if len(pattern) == 0:
        return pattern_found
    for text_index in range(len(text)):
        if pattern_index > 0 and text[text_index] != pattern[pattern_index]:
            pattern_index = 0
            pattern_found = 0
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                pattern_found = text_index
            pattern_index += 1
        if pattern_index > len(pattern) - 1:
            return pattern_found
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index_list = []
    for i in range(len(text)):
        if len(pattern) == 0:
            index_list.append(i)
            continue
        if text[i] == pattern[0]:
            index_list.append(i)
            temp = i
            for j in range(len(pattern)):
                if text[temp] != pattern[j]:
                    del index_list[len(index_list) - 1]
                    break
                elif temp == len(text) - 1 and j < len(pattern) - 1:
                    del index_list[len(index_list) - 1]
                    break
                if temp < len(text) - 1:
                    temp += 1
    return index_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))
    pass


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
