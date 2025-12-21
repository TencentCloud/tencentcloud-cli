**Example 1: 获取实例同步策略列表**



Input: 

```
tccli tcr DescribeReplicationPolicies --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --Page 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ReplicationPolicyInfoList": [
            {
                "ID": "1",
                "Name": "test",
                "Description": "test",
                "Filters": [
                    {
                        "Type": "tag",
                        "Value": "v1"
                    }
                ],
                "Override": true,
                "Enabled": true,
                "SrcResource": "test/event-center/eric:v1 ap-chengdu",
                "DestResource": "tcr-e8pg46c6/event-center/eric ap-guangzhou",
                "CreationTime": "2023-08-01T03:45:03+08:00",
                "UpdateTime": "2023-08-01T03:45:03+08:00"
            }
        ],
        "RequestId": "request-xxxxx"
    }
}
```

