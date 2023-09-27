**Example 1: 查询Nacos类型引擎实例副本信息**

查询Nacos类型引擎实例副本信息

Input: 

```
tccli tse DescribeNacosReplicas --cli-unfold-argument  \
    --InstanceId ins-123456 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Replicas": [
            {
                "Name": "abc",
                "Role": "abc",
                "Status": "abc",
                "SubnetId": "abc",
                "Zone": "abc",
                "ZoneId": "abc",
                "VpcId": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

