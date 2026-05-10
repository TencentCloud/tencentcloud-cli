**Example 1: 用于获取预聚合任务列表**

用于获取预聚合任务列表

Input: 

```
tccli cls DescribeRecordingRuleTask --cli-unfold-argument  \
    --TopicId 539ba7bc-25e2-4696-bde5-0a5567164xxx \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RecordingRuleTaskInfos": [
            {
                "CreateTime": "2024-07-23 11:39:23",
                "CustomMetricLabels": [],
                "DstTopicId": "539ba7bc-25e2-4696-bde5-0a5567164xxx",
                "EnableFlag": 1,
                "HasServicesLog": 2,
                "MetricName": "demo",
                "Name": "test-1234",
                "ProcessDelay": 60,
                "ProcessPeriod": 1,
                "ProcessStartTime": 2024,
                "RecordingRuleContent": "sum by (code)(prometheus_http_requests_total)",
                "Status": 1,
                "TaskId": "938a5abf-f121-4d07-b965-3ae5626d1f43",
                "TopicId": "539ba7bc-25e2-4696-bde5-0a5567164xxx",
                "UpdateTime": "2024-07-23 11:39:23",
                "YamlConfigName": "",
                "YamlId": ""
            }
        ],
        "RequestId": "d64d5787-a440-400f-96ea-d9752a347216",
        "TotalCount": 2
    }
}
```

