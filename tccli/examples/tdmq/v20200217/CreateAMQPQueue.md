**Example 1: 创建AMQP队列**



Input: 

```
tccli tdmq CreateAMQPQueue --cli-unfold-argument  \
    --VHostId test \
    --Remark example \
    --AutoDelete true \
    --Queue test \
    --DeadLetterExchange test-exchange \
    --DeadLetterRoutingKey testKey \
    --ClusterId amqp-dsadasd
```

Output: 
```
{
    "Response": {
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df"
    }
}
```

