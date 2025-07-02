class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       task_counts = Counter(tasks)
       max_freq= max(task_counts.values())

       max_freq_counts=sum(freq == max_freq for freq in task_counts.values())
       idle_time = (max_freq-1)*(n+1)
       min_length = idle_time + max_freq_counts

       return max(len(tasks),min_length)