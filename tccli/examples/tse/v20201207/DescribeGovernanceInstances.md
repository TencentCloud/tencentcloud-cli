**Example 1: 查询治理中心服务实例**



Input: 

```
tccli tse DescribeGovernanceInstances --cli-unfold-argument  \
    --Protocol xx \
    --Service xx \
    --InstanceId xx \
    --Isolate True \
    --Namespace xx \
    --Host xx \
    --HealthStatus True \
    --Offset 1 \
    --InstanceVersion xx \
    --Limit 1 \
    --Metadatas.0.Value xx \
    --Metadatas.0.Key xx
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Protocol": "xx",
                "Weight": 1,
                "Service": "xx",
                "EnableHealthCheck": true,
                "Isolate": true,
                "Ttl": 1,
                "Namespace": "xx",
                "Id": "xx",
                "Healthy": true,
                "Host": "xx",
                "Version": "xx",
                "ModifyTime": "xx",
                "Port": 1,
                "CreateTime": "xx",
                "Metadatas": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

