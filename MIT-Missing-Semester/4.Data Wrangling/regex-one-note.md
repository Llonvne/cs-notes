# Regex-One-Note

**Lesson 1: An Introduction, and the ABCs**

Go ahead and try writing a pattern that matches all three rows, *it may be as simple as the common letters on each line*.
继续尝试编写一个匹配所有三行的模式，它可能就像每行上的常见字母一样简单。

<img src="./assets/CleanShot%202024-01-04%20at%2019.54.23@2x.png" alt="CleanShot 2024-01-04 at 19.54.23@2x" style="zoom:50%;" />

**Solution**

<img src="./assets/CleanShot%202024-01-04%20at%2019.55.21@2x.png" alt="CleanShot 2024-01-04 at 19.55.21@2x" style="zoom:50%;" />

**Lesson 1½: The 123s**

Below are a few more lines of text containing digits. Try writing a pattern that matches all the digits in the strings below, and notice how your pattern matches *anywhere within the string*, not just starting at the first character. We will learn how to control this in a later lesson.
下面是几行包含数字的文本。尝试编写一个匹配下面字符串中所有数字的模式，并注意您的模式如何匹配字符串中的任何位置，而不仅仅是从第一个字符开始。我们将在后面的课程中学习如何控制它。

<img src="./assets/CleanShot%202024-01-04%20at%2019.58.25@2x.png" alt="CleanShot 2024-01-04 at 19.58.25@2x" style="zoom:50%;" />

**Lesson 2: The Dot**

Below are a couple strings with varying characters but the same length. Try to write a single pattern that can match the first three strings, but not the last (to be skipped). You may find that you will have to escape the dot metacharacter to match the period in some of the lines.
下面是几个字符不同但长度相同的字符串。尝试编写一个可以匹配前三个字符串但不能匹配最后一个字符串的模式（要跳过）。您可能会发现必须转义点元字符才能匹配某些行中的句点。

<img src="./assets/CleanShot%202024-01-04%20at%2020.00.07@2x.png" alt="CleanShot 2024-01-04 at 20.00.07@2x" style="zoom:50%;" />

**Solution**

<img src="./assets/CleanShot%202024-01-04%20at%2020.00.49@2x.png" alt="CleanShot 2024-01-04 at 20.00.49@2x" style="zoom:50%;" />

**Lesson 3: Matching specific characters**

Below are a couple lines, where we only want to match the first three strings, but not the last three strings. Notice how we can't avoid matching the last three strings if we use the dot, but have to specifically define what letters to match using the notation above.
下面是几行，我们只想匹配前三个字符串，而不是最后三个字符串。请注意，如果使用点，我们就无法避免匹配最后三个字符串，但必须使用上面的表示法专门定义要匹配的字母。

<img src="./assets/CleanShot%202024-01-04%20at%2020.02.33@2x.png" alt="CleanShot 2024-01-04 at 20.02.33@2x" style="zoom:50%;" />

**Lesson 4: Excluding specific characters**

With the strings below, try writing a pattern that matches only the live animals (hog, dog, but not bog). Notice how most patterns of this type can also be written using the technique from the last lesson as they are really two sides of the same coin. By having both choices, you can decide which one is easier to write and understand when composing your own patterns.

<img src="./assets/CleanShot%202024-01-04%20at%2020.03.18@2x.png" alt="CleanShot 2024-01-04 at 20.03.18@2x" style="zoom:50%;" />

**Lesson 5: Character ranges**

In the exercise below, notice how all the match and skip lines have a pattern, and use the bracket notation to match or skip each character from each line. Be aware that patterns are *case sensitive* and *a-z differs* from *A-Z* in terms of the characters it matches (lower vs upper case).
在下面的练习中，请注意所有匹配和跳过行如何具有模式，并使用括号表示法来匹配或跳过每行中的每个字符。请注意，模式区分大小写，并且 a-z 与 A-Z 的不同之处在于它匹配的字符（小写与大写）。

<img src="./assets/CleanShot%202024-01-04%20at%2020.04.41@2x.png" alt="CleanShot 2024-01-04 at 20.04.41@2x" style="zoom:50%;" />

**Lesson 6: Catching some zzz's**

<img src="./assets/CleanShot%202024-01-04%20at%2020.05.46@2x.png" alt="CleanShot 2024-01-04 at 20.05.46@2x" style="zoom:50%;" />

<img src="./assets/CleanShot%202024-01-04%20at%2020.06.38@2x.png" alt="CleanShot 2024-01-04 at 20.06.38@2x" style="zoom:50%;" />

**Lesson 7: Mr. Kleene, Mr. Kleene**

<img src="./assets/CleanShot%202024-01-05%20at%2010.19.47@2x.png" alt="CleanShot 2024-01-05 at 10.19.47@2x" style="zoom:50%;" />

**Lesson 8: Characters optional**

<img src="./assets/CleanShot%202024-01-05%20at%2010.21.45@2x.png" alt="CleanShot 2024-01-05 at 10.21.45@2x" style="zoom:50%;" />

**Lesson 9: All this whitespace**

<img src="./assets/CleanShot%202024-01-05%20at%2010.24.13@2x.png" alt="CleanShot 2024-01-05 at 10.24.13@2x" style="zoom:50%;" />

**Lesson 10: Starting and ending**

<img src="./assets/CleanShot%202024-01-05%20at%2010.25.01@2x.png" alt="CleanShot 2024-01-05 at 10.25.01@2x" style="zoom:50%;" />

**Lesson 11: Match groups**

<img src="./assets/CleanShot%202024-01-05%20at%2010.27.50@2x.png" alt="CleanShot 2024-01-05 at 10.27.50@2x" style="zoom:50%;" />

**Lesson 12: Nested groups**

<img src="./assets/CleanShot%202024-01-05%20at%2010.29.41@2x.png" alt="CleanShot 2024-01-05 at 10.29.41@2x" style="zoom:50%;" />

**Lesson 13: More group work**

<img src="./assets/CleanShot%202024-01-05%20at%2010.30.25@2x.png" alt="CleanShot 2024-01-05 at 10.30.25@2x" style="zoom:50%;" />

**Lesson 14: It's all conditional**

<img src="./assets/CleanShot%202024-01-05%20at%2010.31.03@2x.png" alt="CleanShot 2024-01-05 at 10.31.03@2x" style="zoom:50%;" />

**Lesson X: Infinity and beyond!**

You've finished the tutorial!

## Additional Problem 

https://regexone.com/problem/matching_decimal_numbers

*待继续*

