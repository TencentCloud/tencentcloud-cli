**Example 1: 更新Topic示例**



Input: 

```
tccli iotexplorer ModifyTopicPolicy --cli-unfold-argument  \
    --ProductId J2CRPPZ8J4 \
    --TopicName $thing/up/J2CRPPZ8J4/d1 \
    --NewTopicName $thing/up/J2CRPPZ8J4/d2 \
    --Privilege 2
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

