class Solution {
    public boolean isPalindrome(String s) {
        /*
        Remove all non-alphanumeric characters 
        Use 2 pointers to check
        */

        String editedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();;
        
        int i = 0;
        int j = editedString.length() - 1;

        while (i <= j) {
            if (editedString.charAt(i) != editedString.charAt(j)) return false;
            i++; 
            j--;
        }

        return true;
    }
}
