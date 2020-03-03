class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if(A + B == 0):
            return ''

        index = 2
        if(A > B):
            tmp_list = 'a' * A
            while(B > 0):
                if(B >= 2 and B >= len(tmp_list[index:])):
                    tmp_list = tmp_list[:index] + 'bb' + tmp_list[index:]
                    index += 2
                    B -= 2
                else:
                    tmp_list = tmp_list[:index] + 'b' + tmp_list[index:]
                    index += 1
                    B -= 1
                index += 2
        else:
            tmp_list = 'b' * B
            while(A > 0):
                if(A >= 2 and A >= len(tmp_list[index:])):
                    tmp_list = tmp_list[:index] + 'aa' + tmp_list[index:]
                    index += 2
                    A -= 2
                else:
                    tmp_list = tmp_list[:index] + 'a' + tmp_list[index:]
                    index += 1
                    A -= 1
                index += 2

        return tmp_list