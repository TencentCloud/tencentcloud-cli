**Example 1: 获取Amqp Vhost列表**



Input: 

```
tccli tdmq DescribeAMQPVHosts --cli-unfold-argument  \
    --NameKeyword test \
    --ClusterId amqp-dsadasd \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "VHosts": [
            {
                "Username": "xx",
                "Remark": "xx",
                "Password": "xx",
                "UpdateTime": 1,
                "MsgTtl": 1,
                "Status": 0,
                "VHostId": "test",
                "CreateTime": 1560000000
            }
        ],
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df",
        "TotalCount": 1
    }
}
```

