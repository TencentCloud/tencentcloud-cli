**Example 1: 更新Vhost**



Input: 

```
tccli tdmq ModifyAMQPVHost --cli-unfold-argument  \
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

