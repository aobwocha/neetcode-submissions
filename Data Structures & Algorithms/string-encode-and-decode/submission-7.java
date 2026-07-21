class Solution {

    public String encode(List<String> strs) {
        if (strs.size() == 0) {
            return "±";
        }

        String result = "";
        for (int i = 0; i < strs.size(); i++) {
            String currentWord = strs.get(i);
            if (i == 0) {
                result = currentWord;
            } else {
                result += ("±" + currentWord);
            }
        }
        return result;
    }

    public List<String> decode(String str) {
        if (str.equals("±")) {
            return new ArrayList<>();
        }

        List<String> result = new ArrayList<>();
        int prevChar = 0;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '±') {
                result.add(str.substring(prevChar, i));
                prevChar = i+1;
            }
        }
        result.add(str.substring(prevChar, str.length()));
        return result;

        
    }
}
