**Example 1: 修改主题属性**



Input: 

```
tccli tdmq ModifyCmqTopicAttribute --cli-unfold-argument  \
    --TopicName test-topic \
    --MaxMsgSize 1240 \
    --MsgRetentionSeconds 43200 \
    --Trace True
```

Output: 
```
{
    "Response": {
        "RequestId": "8a04c6b1-dec5-4979-b3b2-34ab3b3402b2"
    }
}
```

