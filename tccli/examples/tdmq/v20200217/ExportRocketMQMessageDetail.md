**Example 1: demo**

导出消息详情

Input: 

```
tccli tdmq ExportRocketMQMessageDetail --cli-unfold-argument  \
    --ClusterId abc \
    --EnvironmentId abc \
    --TopicName abc \
    --MsgId abc \
    --DeadLetterMsg True \
    --IncludeMsgBody True
```

Output: 
```
{
    "Response": {
        "MsgId": "abc",
        "BornTimestamp": 0,
        "StoreTimestamp": 0,
        "BornHost": "abc",
        "MsgTag": "abc",
        "MsgKey": "abc",
        "Properties": "abc",
        "ReConsumeTimes": 1,
        "MsgBody": "abc",
        "MsgBodyCRC": 0,
        "MsgBodySize": 1,
        "RequestId": "abc"
    }
}
```

