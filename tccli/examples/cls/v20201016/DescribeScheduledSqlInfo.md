**Example 1: 获取ScheduledSql任务列表**



Input: 

```
tccli cls DescribeScheduledSqlInfo --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e1700c27-xxxx-xxxx-806f-eece0a0e756e",
        "ScheduledSqlTaskInfos": [
            {
                "CreateTime": "2024-12-25 15:07:41",
                "DstResource": {
                    "BizType": 0,
                    "CustomMetricLabels": [],
                    "CustomTime": "",
                    "MetricLabels": [],
                    "MetricName": "",
                    "Region": "ap-chengdu",
                    "TopicId": "d30a5165-xxxx-xxxx-9e94-fb733d2c1c0e"
                },
                "EnableFlag": 1,
                "HasServicesLog": 2,
                "Name": "scheduler_sql_delete_task",
                "ProcessDelay": 60,
                "ProcessEndTime": "",
                "ProcessPeriod": 1,
                "ProcessStartTime": "2024-12-25 15:07:00",
                "ProcessTimeWindow": "@m-1m,@m",
                "ProcessType": 1,
                "ScheduledSqlContent": "* | select count(*) as c limit 10000",
                "SrcTopicId": "fe4e7d35-xxxx-xxxx-82e1-2762471b0928",
                "SrcTopicName": "",
                "SrcTopicRegion": "ap-chengdu",
                "Status": 1,
                "SyntaxRule": 1,
                "TaskId": "44bb210d-xxxx-xxxx-8f7d-7fc5170553d4",
                "UpdateTime": "2024-12-25 15:07:41"
            }
        ],
        "TotalCount": 15
    }
}
```

