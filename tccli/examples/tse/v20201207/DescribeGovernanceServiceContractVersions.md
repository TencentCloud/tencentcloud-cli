**Example 1: 查询服务下契约版本列表**

查询服务下契约版本列表

Input: 

```
tccli tse DescribeGovernanceServiceContractVersions --cli-unfold-argument  \
    --InstanceId ins-id \
    --Namespace namespace \
    --Service service
```

Output: 
```
{
    "Response": {
        "GovernanceServiceContractVersions": [
            {
                "Version": "1.0",
                "Name": "name",
                "Key": "key"
            }
        ],
        "RequestId": "req-id"
    }
}
```

