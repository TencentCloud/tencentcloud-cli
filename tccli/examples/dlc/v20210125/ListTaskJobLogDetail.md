**Example 1: 查询日志详情**

查询spark 作业任务的日志详情

Input: 

```
tccli dlc ListTaskJobLogDetail --cli-unfold-argument  \
    --TaskId c88e7e08-71fc-4a74-8164-4c4ff4605e53 \
    --StartTime 1735991656000 \
    --EndTime 1736510056000 \
    --Limit 1000 \
    --Context  \
    --Asc True \
    --Filters.0.Name spark-job-log-name \
    --Filters.0.Values kyuubi-spark-batch-f2ee3489-ab52-4ade-bf88-416142bc2bc0-driver \
    --BatchId 
```

Output: 
```
{
    "Response": {
        "Context": "",
        "ListOver": true,
        "Results": [
            {
                "Time": 0,
                "TopicId": "7f0ea2ee-*-*-*-*",
                "TopicName": "eks-cls",
                "LogJson": "25/01/10 19:15:52 INFO Thread-1 BufferPool: Begin to release the buffers.",
                "PkgLogId": "1835035"
            }
        ],
        "LogUrl": "",
        "RequestId": "ead726f9-1efa-4051-b082-7aec472a580f"
    }
}
```

