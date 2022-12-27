**Example 1: 获取实时会话统计详情**



Input: 

```
tccli dbbrain DescribeProxyProcessStatistics --cli-unfold-argument  \
    --InstanceId redis-test \
    --Product redis \
    --Limit 20 \
    --InstanceProxyId b237ff3c5f30b0
```

Output: 
```
{
    "Response": {
        "RequestId": "099479c0-7b7c-11ed-8d71-fdsafda",
        "ProcessStatistics": {}
    }
}
```

