**Example 1: 示例**

demo

Input: 

```
tccli tdmq DescribeMqMsgTrace --cli-unfold-argument  \
    --EnvironmentId xx \
    --Protocol xx \
    --MsgId xx \
    --ClusterId xx \
    --TopicName xx \
    --GroupName xx \
    --QueueName xx \
    --QueryDlqMsg False
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Stage": "xx",
                "Data": "xx"
            }
        ],
        "ShowTopicName": "xx",
        "RequestId": "xx"
    }
}
```

