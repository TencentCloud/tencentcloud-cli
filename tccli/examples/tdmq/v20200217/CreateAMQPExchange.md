**Example 1: 创建AMQP Exchange**



Input: 

```
tccli tdmq CreateAMQPExchange --cli-unfold-argument  \
    --VHosts test \
    --Remark example \
    --Type Topic \
    --Exchange dasd \
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

