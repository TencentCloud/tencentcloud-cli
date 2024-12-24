**Example 1: 查询服务实例**



Input: 

```
tccli tse DescribeGovernanceInstances --cli-unfold-argument  \
    --Service service \
    --Namespace namespace \
    --Host 127.0.0.1 \
    --InstanceVersion prod \
    --Protocol tcp \
    --HealthStatus True \
    --Isolate True \
    --Metadatas.0.Key key \
    --Metadatas.0.Value value \
    --Offset 1 \
    --Limit 1 \
    --InstanceId ins-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Id": "id",
                "Service": "service-name",
                "Namespace": "namespace",
                "Host": "127.0.0.1",
                "Port": 1,
                "Protocol": "tcp",
                "Version": "1",
                "Weight": 1,
                "EnableHealthCheck": true,
                "Healthy": true,
                "Isolate": true,
                "CreateTime": "2024-10-08 10:00:00",
                "ModifyTime": "2024-10-08 10:00:00",
                "Metadatas": [
                    {
                        "Key": "key",
                        "Value": "value"
                    }
                ],
                "Ttl": 1,
                "InstanceVersion": "prod",
                "HealthStatus": "health",
                "Comment": "comment"
            }
        ],
        "RequestId": "req-id"
    }
}
```

