**Example 1: 修改主题属性**



Input: 

```
tccli tdmq ModifyCmqTopicAttribute --cli-unfold-argument  \
    --MaxMsgSize 1 \
    --TopicName xx \
    --Trace True \
    --MsgRetentionSeconds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "8a04c6b1-dec5-4979-b3b2-34ab3b3402b2"
    }
}
```

