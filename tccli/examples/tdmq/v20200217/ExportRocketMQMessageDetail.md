**Example 1: demo**

导出消息详情

Input: 

```
tccli tdmq ExportRocketMQMessageDetail --cli-unfold-argument  \
    --ClusterId xx \
    --EnvironmentId xx \
    --TopicName xx \
    --MsgId xx \
    --DeadLetterMsg True \
    --IncludeMsgBody True
```

Output: 
```
{
    "Response": {
        "MsgId": "xx",
        "BornTimestamp": 0,
        "StoreTimestamp": 0,
        "BornHost": "xx",
        "MsgTag": "xx",
        "MsgKey": "xx",
        "Properties": "xx",
        "ReConsumeTimes": 1,
        "MsgBody": "xx",
        "MsgBodyCRC": 0,
        "MsgBodySize": 1,
        "RequestId": "xx"
    }
}
```

