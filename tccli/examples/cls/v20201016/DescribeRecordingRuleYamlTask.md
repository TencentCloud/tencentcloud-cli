**Example 1: 用于获取yaml预聚合任务列表**

用于获取yaml预聚合任务列表

Input: 

```
tccli cls DescribeRecordingRuleYamlTask --cli-unfold-argument  \
    --TopicId 539ba7bc-25e2-4696-bde5-0a5567164xxx \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RecordingRuleYamlTaskInfos": [],
        "RequestId": "76f39b5e-8476-4247-9331-9d415530d447",
        "TotalCount": 0
    }
}
```

