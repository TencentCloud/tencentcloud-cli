**Example 1: 正常响应**

查询生产者客户端列表成功。

Input: 

```
tccli tdmq DescribeRocketMQProducers --cli-unfold-argument  \
    --ClusterId rocketmq-5kze4gr222mx \
    --NamespaceId test_ns \
    --Topic test_topic \
    --Offset 0 \
    --Limit 0 \
    --Filters.0.Name CliendId \
    --Filters.0.Values 10.10.10.10@abc
```

Output: 
```
{
    "Response": {
        "Producers": [
            {
                "ClientId": "10.10.10.10@abc",
                "ClientIp": "10.10.10.10",
                "Language": "JAVA",
                "Version": "v5_0_5",
                "LastUpdateTimestamp": 1723195366688
            }
        ],
        "TotalCount": 0,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

