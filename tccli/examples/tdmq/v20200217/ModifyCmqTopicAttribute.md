**Example 1: 修改主题属性**



Input: 

```
tccli tdmq ModifyCmqTopicAttribute --cli-unfold-argument  \
    --TopicName abc \
    --MaxMsgSize 1 \
    --MsgRetentionSeconds 1 \
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

