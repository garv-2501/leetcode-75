# I don't know why my solution is just not processing in leetcode. Solution2 in mine

class Solution:
  def compress(self, chars: list[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1
          
    print(chars)
    return ans


class Solution2:
    def compress(self, chars: list[str]) -> int:
        chars.append("-1")
        output = []
        currentCharacter = chars[0]
        output.append(currentCharacter)
        counter = 0
        for character in chars:
            if currentCharacter == character:
                counter += 1
            elif character == "-1":
                if counter > 1:
                    output.append(counter)
                break
            else:
                if counter > 1:
                    output.append(counter)
                currentCharacter = character
                output.append(currentCharacter)
                counter = 1

        chars = chars[:-1]
        for i in range(len(output)):
            chars[i]=output[i]
        print(chars)
        return len(output)


trial = Solution()
trial2 = Solution()
print(trial.compress(["a","a","b","b","b","b","b","b"]))
print(trial2.compress(["a","a","b","b","b","b","b","b"]))


