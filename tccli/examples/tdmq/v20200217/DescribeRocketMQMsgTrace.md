**Example 1: 查询消息轨迹**

查询消息轨迹

Input: 

```
tccli tdmq DescribeRocketMQMsgTrace --cli-unfold-argument  \
    --ClusterId abc \
    --EnvironmentId abc \
    --TopicName abc \
    --MsgId abc \
    --GroupName abc \
    --QueryDLQMsg True
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Stage": "abc",
                "Data": "abc"
            }
        ],
        "ShowTopicName": "abc",
        "RequestId": "abc"
    }
}
```

