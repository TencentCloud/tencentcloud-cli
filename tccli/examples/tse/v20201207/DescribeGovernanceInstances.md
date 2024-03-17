**Example 1: 查询服务实例**



Input: 

```
tccli tse DescribeGovernanceInstances --cli-unfold-argument  \
    --Service abc \
    --Namespace abc \
    --Host abc \
    --InstanceVersion abc \
    --Protocol abc \
    --HealthStatus True \
    --Isolate True \
    --Metadatas.0.Key abc \
    --Metadatas.0.Value abc \
    --Offset 1 \
    --Limit 1 \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Id": "abc",
                "Service": "abc",
                "Namespace": "abc",
                "Host": "abc",
                "Port": 1,
                "Protocol": "abc",
                "Version": "abc",
                "Weight": 1,
                "EnableHealthCheck": true,
                "Healthy": true,
                "Isolate": true,
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "Metadatas": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Ttl": 1,
                "InstanceVersion": "abc",
                "HealthStatus": "abc",
                "Comment": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

