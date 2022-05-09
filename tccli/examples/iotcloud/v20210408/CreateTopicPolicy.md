**Example 1: 创建Topic示例**



Input: 

```
tccli iotcloud CreateTopicPolicy --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --TopicName abc \
    --Privilege 2 \
    --BrokerSubscribe.ProductId 11LAWZ3J2D \
    --BrokerSubscribe.DeviceName device1
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

