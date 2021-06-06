
def find_ans(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == sum:
                return ([arr[i],arr[j]])

def main():
    arr = input("Please enter the array: ")
    arr = [int(n) for n in arr.split()]
    sum = int(input("Target sum: "))
    ans = find_ans(arr, sum)
    print("Result: ", ans)

if __name__ == "__main__":
    main()