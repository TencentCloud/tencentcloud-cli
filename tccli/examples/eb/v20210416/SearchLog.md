**Example 1: 事件查询**

事件查询

Input: 

```
tccli eb SearchLog --cli-unfold-argument  \
    --StartTime 1673233483024 \
    --EndTime 1673838283024 \
    --EventBusId eb-xxxxx \
    --Page 1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "Results": [
            {
                "Timestamp": "2023-01-09 11:04:43",
                "Message": "event-data",
                "Source": "ckafka.cloud.tencent",
                "Type": "消费分组成员心跳超时(ckafka:ErrorEvent:ConsumerGroupMemberHeartbeatTimeout)",
                "RuleIds": "rule-gr*jo",
                "Subject": "ckafka-xxx",
                "Region": "ap-guangzhou",
                "Status": "1"
            }
        ],
        "Total": 1,
        "Limit": 10,
        "Page": 1
    }
}
```

