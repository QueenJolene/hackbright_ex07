from sys import argv

program, file_name = argv


def count_words(file_name): 
    word_file = open(file_name)
    wordline_list = []
    for line in word_file:
        stripped_line = line.strip()
        words_list = stripped_line.split()
        wordline_list = wordline_list + words_list 
    return wordline_list

def word_count(wordline_list):
    word_count_dict ={}
    for word in wordline_list:
        word = word.lower().strip(",?.")
        if word in word_count_dict:
            word_count_dict[word] = word_count_dict[word] + 1
        elif word not in word_count_dict:
            word_count_dict[word] = 1

    return word_count_dict


def main():
    word_count_dict = word_count(count_words(file_name))

    alpha_sorted_freq_tuple_list = sorted(word_count_dict.items())
    freq_sorted_tuple_list = sorted(alpha_sorted_freq_tuple_list, key = lambda word: word[1], reverse = True)
    # print sorted_tuple_list
    for key, value in freq_sorted_tuple_list:
        print key, value

if __name__ == '__main__':
    main()
