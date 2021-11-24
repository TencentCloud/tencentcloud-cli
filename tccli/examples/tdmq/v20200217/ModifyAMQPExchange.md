**Example 1: 更新Amqp交换机**



Input: 

```
tccli tdmq ModifyAMQPExchange --cli-unfold-argument  \
    --VHostId test \
    --Remark example \
    --ClusterId amqp-dsadasd \
    --Exchange test
```

Output: 
```
{
    "Response": {
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df"
    }
}
```

