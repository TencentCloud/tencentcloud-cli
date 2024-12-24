**Example 1: 查询服务契约定义列表**

查询服务契约定义列表

Input: 

```
tccli tse DescribeGovernanceServiceContracts --cli-unfold-argument  \
    --InstanceId ins-id \
    --Namespace namespace \
    --Service service \
    --Name name \
    --ContractVersion 1.0 \
    --Protocol tcp \
    --Brief True \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Size": 0,
        "ServiceContracts": [
            {
                "Name": "name",
                "Namespace": "namespace",
                "Protocol": "tcp",
                "ID": "id",
                "Service": "service",
                "Version": "1.0",
                "Revision": "hash",
                "Content": "content",
                "CreateTime": "2024-10-08 10:00:00",
                "ModifyTime": "2024-10-08 10:00:00",
                "Interfaces": [
                    {
                        "ID": "id",
                        "Method": "get",
                        "Path": "/path",
                        "Content": "content",
                        "Source": "api",
                        "Revision": "hash",
                        "CreateTime": "2024-10-08 10:00:00",
                        "ModifyTime": "2024-10-08 10:00:00",
                        "Name": "name"
                    }
                ]
            }
        ],
        "RequestId": "req-id"
    }
}
```

