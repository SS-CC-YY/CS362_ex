def word_reverse(in_put):
    in_put = in_put.split(' ')
    out_put = ' '.join(in_put[::-1])
    return out_put

def main():
    sentence = input("Enter a sentence: ")
    out_put = word_reverse(sentence)
    print("Result: ", out_put)

if __name__ == "__main__":
    main()