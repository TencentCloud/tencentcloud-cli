**Example 1: 获取ScheduledSql任务列表**



Input: 

```
tccli cls DescribeScheduledSqlInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "ScheduledSqlTaskInfos": [
            {
                "Status": 0,
                "EnableFlag": 0,
                "UpdateTime": "xx",
                "Name": "xx",
                "DstResource": {
                    "TopicId": "xx",
                    "Region": "xx"
                },
                "ProcessTimeWindow": "xx",
                "ProcessPeriod": 0,
                "ProcessStartTime": "xx",
                "SrcTopicRegion": "xx",
                "SrcTopicName": "xx",
                "ScheduledSqlContent": "xx",
                "SrcTopicId": "xx",
                "ProcessDelay": 0,
                "TaskId": "xx",
                "ProcessType": 0,
                "CreateTime": "xx",
                "ProcessEndTime": "xx"
            }
        ]
    }
}
```

