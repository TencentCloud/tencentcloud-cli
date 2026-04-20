**Example 1: 查看实例公网IP白名单配置**

查看实例公网IP白名单配置

Input: 

```
tccli ckafka DescribeAccessPolicy --cli-unfold-argument  \
    --InstanceId ckafka-ay3z77qe \
    --RouteId 137946
```

Output: 
```
{
    "Response": {
        "Result": {
            "IpWhitelist": [
                {
                    "CidrBlock": "127.0.0.1",
                    "PolicyDescription": "test-description"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "01fbfd54-f0ec-4bbf-ba21-211a845bfa3b"
    }
}
```

