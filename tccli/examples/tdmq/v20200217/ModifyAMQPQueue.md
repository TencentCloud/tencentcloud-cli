**Example 1: 更新Amqp队列**



Input: 

```
tccli tdmq ModifyAMQPQueue --cli-unfold-argument  \
    --VHostId test \
    --AutoDelete true \
    --Queue test \
    --DeadLetterExchange test \
    --DeadLetterRoutingKey testKey \
    --Remark xxx \
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

