**Example 1: 创建Amqp Vhost**



Input: 

```
tccli tdmq CreateAMQPVHost --cli-unfold-argument  \
    --VHostId test \
    --Remark example \
    --MsgTtl 1 \
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

