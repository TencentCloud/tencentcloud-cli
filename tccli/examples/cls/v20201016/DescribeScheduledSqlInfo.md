**Example 1: 获取ScheduledSql任务列表**



Input: 

```
tccli cls DescribeScheduledSqlInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb5xxxx",
        "ScheduledSqlTaskInfos": [
            {
                "Status": 1,
                "EnableFlag": 2,
                "UpdateTime": "2023-07-28 11:36:00",
                "Name": "test",
                "DstResource": {
                    "TopicId": "6ef60bec-0242-43af-bb20-270359fb5xxx",
                    "Region": "ap-guangzhou",
                    "BizType": 1,
                    "MetricName": "pv"
                },
                "ProcessTimeWindow": "@m-15m,@m",
                "ProcessPeriod": 5,
                "ProcessStartTime": "2023-07-28 11:36:00",
                "SrcTopicRegion": "ap-guangzhou",
                "SrcTopicName": "test-topic",
                "ScheduledSqlContent": "* | select count(*) as pv",
                "SrcTopicId": "6ef60bec-0242-43af-bb20-270359fb5xxxx",
                "ProcessDelay": 60,
                "TaskId": "6ef60bec-0242-43af-bb20-270359fb5xxxx",
                "ProcessType": 1,
                "CreateTime": "2023-07-28 11:36:00",
                "ProcessEndTime": "2023-07-28 11:36:00",
                "SyntaxRule": 0
            }
        ]
    }
}
```

