class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)
            return 0;
        int head_ptr = 0;
        int tail_ptr = 1;
        int length = tail_ptr-head_ptr;
        for (int i=1; i<s.size(); i++){
            bool isDuplicate = false;
            int check_ptr = head_ptr;
            while (check_ptr < tail_ptr){
                if (s[i] == s[check_ptr]){
                    head_ptr += 1;
                    isDuplicate = true;
                }

                if (isDuplicate){
                    check_ptr = head_ptr;
                    isDuplicate = false;
                }
                else{
                    check_ptr ++;
                }
            }
            if (!isDuplicate){
                tail_ptr += 1;
                if (tail_ptr-head_ptr > length)
                    length = tail_ptr-head_ptr;
            }
        }
        return length;
    }
};