**Example 1: 获取作业信息列表**

获取作业信息列表

Input: 

```
tccli dlc DescribeJobs --cli-unfold-argument  \
    --Keyword 049e684fccec11ef81db5254009c9d07 \
    --Pattern pattern \
    --Limit 10 \
    --Offset 0 \
    --Sort create-time \
    --Asc True
```

Output: 
```
{
    "Response": {
        "JobList": [
            {
                "JobName": "049e684fccec11ef81db5254009c9d07",
                "JobStatus": -1,
                "StatisticInfo": {
                    "CreateTime": 1736249953358,
                    "EndTime": 1736249956847,
                    "RowsAffect": 0,
                    "StartTime": 1736249956847,
                    "TaskId": "049e684fccec11ef81db5254009c9d07",
                    "TotalProcessedBytes": 0,
                    "TotalTime": 3489,
                    "UsedTime": 0
                }
            }
        ],
        "RequestId": "6102d6b7-df85-425c-a09d-30dbb5234890",
        "TotalCount": 1
    }
}
```

