**Example 1: 查询作业信息**



Input: 

```
tccli dlc DescribeJob --cli-unfold-argument  \
    --JobId 9e20f9c021cb11ec835f5254006c64af
```

Output: 
```
{
    "Response": {
        "RequestId": "9328049f-30bc-4feb-aecf-e3b4ff2d1b00",
        "JobName": "name",
        "JobConfiguration": "[{\"key\":\"value\"}]",
        "JobStatus": 2,
        "StatisticInfo": {
            "TaskId": "9e20f9c021cb11ec835f5254006c64af",
            "TotalProcessedBytes": 850363,
            "UsedTime": 1761,
            "TotalTime": 2000,
            "CreateTime": "1632991895728",
            "EndTime": "1632991897728",
            "StartTime": "1632991896728",
            "RowsAffect": "59378"
        }
    }
}
```

