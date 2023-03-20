# CleanCode

**Here are some ways to write clean code.**

- [Naming things meaningfully](https://github.com/mallycrip/_Clean_Code/tree/master/%EC%9D%98%EB%AF%B8%20%EC%9E%88%EA%B2%8C%20%EC%9D%B4%EB%A6%84%20%EC%A0%95%ED%95%98%EA%B8%B0)
- [Functions](https://github.com/mallycrip/_Clean_Code/tree/master/%ED%95%A8%EC%88%98)
- [Comments](https://github.com/mallycrip/_Clean_Code/blob/master/%EC%A3%BC%EC%84%9D)
- [Formatting](https://github.com/mallycrip/_Clean_Code/tree/master/%ED%98%95%EC%8B%9D)
- [Unit tests](https://github.com/mallycrip/_Clean_Code/tree/master/%EB%8B%A8%EC%9C%84%20%ED%85%8C%EC%8A%A4%ED%8A%B8)
- [Objects and data structures](https://github.com/mallycrip/_Clean_Code/tree/master/%EA%B0%9D%EC%B2%B4%EC%99%80%20%EC%9E%90%EB%A3%8C%20%EA%B5%AC%EC%A1%B0)
- [Error handling](https://github.com/mallycrip/_Clean_Code/tree/master/%EC%98%A4%EB%A5%98%20%EC%B2%98%EB%A6%AC)
- [Boundaries](https://github.com/mallycrip/_Clean_Code/tree/master/%EA%B2%BD%EA%B3%84)
- [Classes](https://github.com/mallycrip/_Clean_Code/tree/master/%ED%81%B4%EB%9E%98%EC%8A%A4)

## More than 80% of software is maintenance.

### 5S principles of TPM focused on maintenance

- Sort (Seiri): Know where everything is through appropriate naming conventions.
- Set in order (Seiton): Code should be where everyone expects it to be.
- Shine (Seiso): Remove unnecessary parts such as comments.
- Standardize (Seiketsu): The group must agree on how to clean the workspace. Standards must be established.
- Sustain/self-discipline (Shutsuke): Follow conventions, frequently review your work, and willingly make changes.

### The cost of bad code

**Bad code significantly slows down development speed.** As bad code accumulates, team productivity decreases. When productivity decreases, management will try to recover it by hiring new resources. However, new resources often lack knowledge of system design and are pressured to increase productivity, leading to the production of even worse code. **Producing bad code is not an issue with management.** The problem is following the words of a manager who does not understand the risks of bad code. **The only way to develop quickly and meet deadlines is to make a habit of keeping the code clean.** If you don't read the surrounding code, you can't write new code. If the surrounding code is easy to read, the new code is also easy to write. If you're in a hurry, want to write easily, or want to finish quickly, make it easy to read.

## Programmers' definition of clean code

- Code that minimizes `dependencies` and expresses them clearly
- Code that maintains optimal `performance` (not just speed, but also resource utilization, etc.)
- Code that is thoroughly and meticulously written, paying attention to every detail
- Code that contains clear `abstractions` and simple control statements for necessary content only
- Code that is easy for others to fix
- Code that has `test cases` and passes all `tests`
- Code that minimizes duplication and reduces classes, methods, functions, etc.
