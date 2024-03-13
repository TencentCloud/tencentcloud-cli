**Example 1: 获取kafka用户信息**



Input: 

```
tccli cls DescribeKafkaUser --cli-unfold-argument  \
    --UserName ANONYMOUS
```

Output: 
```
{
    "Response": {
        "UserName": "ANONYMOUS",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

