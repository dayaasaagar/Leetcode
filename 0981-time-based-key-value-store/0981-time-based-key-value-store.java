class TimeMap {

    private Map<String, List<Pair>> map;
    public TimeMap() {

            map = new HashMap<>();
        
    }
    
    public void set(String key, String value, int timestamp) {
        map.putIfAbsent(key, new ArrayList<>());
        map.get(key).add(new Pair(timestamp,value));
        
    }
    
    public String get(String key, int timestamp) {
        
        if(!map.containsKey(key)) return "";

        //retrieve the inner list of the keys
        List<Pair> pairs = map.get(key);

        int low =0;
        int high = pairs.size()-1;
        String result = "";

        while(low<=high)
        {
            int mid = (low+high)/2;
            if(pairs.get(mid).timestamp==timestamp)
            return pairs.get(mid).value;

            if(pairs.get(mid).timestamp<timestamp)
            {   result= pairs.get(mid).value;
                low = mid+1;
            }
            else
            {
                high = mid-1;

            }

        }
        return result;
    }
    

    class Pair
    {
        String value;
        int timestamp;

        public Pair(int timestamp,String value)
        {
            this.value = value;
            this.timestamp = timestamp;
        }
    }
    
    
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */