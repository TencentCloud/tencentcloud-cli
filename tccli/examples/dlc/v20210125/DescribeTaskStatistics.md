**Example 1: 获取任务统计信息**



Input: 

```
tccli dlc DescribeTaskStatistics --cli-unfold-argument  \
    --TaskId 4ad30ca9-8b0e-499f-b4e1-d6e43ba0e564
```

Output: 
```
{
    "Response": {
        "RequestId": "9328049f-30bc-4feb-aecf-e3b4ff2d1b00",
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

