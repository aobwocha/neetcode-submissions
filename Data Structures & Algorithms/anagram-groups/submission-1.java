class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < strs.length; i++) {
            String currentWord = strs[i];
            boolean added = false;
            for (int j = 0; j < result.size(); j++) {
                if (isAnagram(currentWord, result.get(j).get(0))) {
                    result.get(j).add(currentWord);
                    added = true;
                }
            }
            if (added == false) {
                List<String> newList = new ArrayList<>();
                newList.add(currentWord);
                result.add(newList);
            }
        }

        return result;
    }

    public boolean isAnagram(String firstWord, String secondWord) {
        if (firstWord.length() != secondWord.length()) return false;
        
        Map<Character, Integer> countMap = new HashMap<>();

        for (char c : firstWord.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }

        for (char c : secondWord.toCharArray()) {
            int count = countMap.getOrDefault(c, 0);
            if (count == 0) return false;
            countMap.put(c, count - 1);
        }

        return true;
    }
}
