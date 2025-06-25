**Example 1: 查询消费组下的客户端连接**

查询消费组下的客户端连接

Input: 

```
tccli trocket DescribeConsumerClientList --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup group \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [],
        "RequestId": "c2d581fa-d7b2-453c-ba1a-65c0e507a533",
        "TotalCount": 0
    }
}
```

