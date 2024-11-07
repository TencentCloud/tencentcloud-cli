**Example 1: 示例**

demo

Input: 

```
tccli tdmq DescribeMqMsgTrace --cli-unfold-argument  \
    --Protocol pulsar \
    --ClusterId pulsar-pnvjp9mbd947 \
    --EnvironmentId devNs \
    --TopicName devTopic \
    --QueueName devCmq \
    --MsgId 29292216:15:3 \
    --GroupName devName \
    --QueryDlqMsg True
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Stage": "devInfo",
                "Data": "2023-07-20 10:35:17"
            }
        ],
        "ShowTopicName": "devTopic",
        "RequestId": "722558eb-36dc-4643-854f-aa7436b83125"
    }
}
```

