**Example 1: 获取AMQP Exchange列表**



Input: 

```
tccli tdmq DescribeAMQPExchanges --cli-unfold-argument  \
    --FilterName test \
    --ClusterId amqp-dsadasd \
    --FilterInternal false \
    --VHostId test \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df",
        "Exchanges": [
            {
                "Remark": "xx",
                "Name": "test",
                "DestBindedNum": 1,
                "UpdateTime": 1,
                "SourceBindedNum": 1,
                "Internal": true,
                "Type": "Topic",
                "CreateTime": 100000000
            }
        ]
    }
}
```

