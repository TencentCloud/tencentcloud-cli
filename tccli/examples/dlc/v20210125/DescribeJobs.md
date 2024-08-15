**Example 1: 获取作业信息列表**



Input: 

```
tccli dlc DescribeJobs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "JobList": [
            {
                "JobName": "abc",
                "StatisticInfo": {
                    "TaskId": "abc",
                    "TotalProcessedBytes": 0,
                    "UsedTime": 0,
                    "CreateTime": 0,
                    "EndTime": 0,
                    "StartTime": 0,
                    "RowsAffect": 0,
                    "TotalTime": 0
                },
                "JobConfiguration": "abc",
                "JobStatus": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

