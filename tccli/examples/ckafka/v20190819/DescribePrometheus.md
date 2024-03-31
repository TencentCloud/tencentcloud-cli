**Example 1: 获取实例Prometheus信息**



Input: 

```
tccli ckafka DescribePrometheus --cli-unfold-argument  \
    --InstanceId ckafka-xxx
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Type": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

