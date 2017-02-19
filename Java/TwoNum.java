import java.util.HashMap;
import java.util.Map;

public class TwoNum {
	 public int[] twoSum(int[] nums, int target) {
	        int[] result = new int[2];
	        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
	        for(int index = 0, length = nums.length; index < length; ++index){
	        	if (map.containsKey(target - nums[index])){
	        		result[0] = map.get(target - nums[index]);
	        		result[1] = index;
	        	}else{
	        		map.put(nums[index], index);
	        	}
	        }
	        return result;
	    }
	 
	 public static void main(String[] args) {
		 
	}
}

