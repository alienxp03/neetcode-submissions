class Solution {
    public boolean isValid(String s) {
                Stack<Character> stack = new Stack<>();
        Map<Character, Character> hash = new HashMap<>();
        hash.put(')', '(');
        hash.put('}', '{');
        hash.put(']', '[');

        for(char ch : s.toCharArray()) {
            if(hash.containsKey(ch)) {
                if (!stack.isEmpty() && hash.get(ch) == stack.peek()) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }

        return stack.empty();
    }
}
