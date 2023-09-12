**Example 1: 查询主题详情**

查询主题详情

Input: 

```
tccli trocket DescribeTopic --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic test \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CreatedTime": 1683601674000,
        "InstanceId": "rmq-72mo3a9o",
        "LastUpdateTime": 0,
        "Remark": "remoark",
        "RequestId": "f7f7ba8a-4335-4adb-9186-680b91502c42",
        "SubscriptionCount": 0,
        "SubscriptionData": [],
        "Topic": "test",
        "TopicType": "NORMAL"
    }
}
```

