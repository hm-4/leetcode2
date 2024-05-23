class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [0] # coresponding to temperatures[0], index value.
        toc_ptr = 0
        output = [0]*len(temperatures)

        for i in range(1, len(temperatures)):
            # print()
            # print(temperatures[i])
            if temperatures[i] <= temperatures[stack[toc_ptr]]:
                stack.append(i)
                toc_ptr += 1
                # print("\nin: ", 1)
                # print(output)
                # print(stack)
                # print(toc_ptr)
            else:
                while toc_ptr >=0 and temperatures[i] > temperatures[stack[toc_ptr]]:
                    # print("\nin: ", 2)
                    # print(output)
                    # print(stack)
                    # print(toc_ptr)
                    output[stack[toc_ptr]] = i - stack[toc_ptr]
                    stack.pop()
                    toc_ptr -= 1
                stack.append(i)
                toc_ptr += 1
            # print("\nloop end: ")
            # print(output)
            # print(stack)
            # print(toc_ptr)
        return output




        