**Example 1: 更新Topic示例**



Input: 

```
tccli iotcloud UpdateTopicPolicy --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --TopicName abc \
    --NewTopicName ABC \
    --Privilege 2 \
    --BrokerSubscribe.ProductId 11LAWZ3J2D \
    --BrokerSubscribe.DeviceName device1
```

Output: 
```
{
    "Response": {}
}
```

