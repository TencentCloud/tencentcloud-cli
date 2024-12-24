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
                "Name": "name",
                "Role": "node",
                "Status": "running",
                "SubnetId": "subnet-id",
                "Zone": "ap-guangzhou-1",
                "ZoneId": "100001",
                "VpcId": "vpc-id"
            }
        ],
        "TotalCount": 1,
        "RequestId": "req-id"
    }
}
```

