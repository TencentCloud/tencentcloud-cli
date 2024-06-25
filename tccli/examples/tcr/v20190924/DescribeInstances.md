**Example 1: 查看实例列表**



Input: 

```
tccli tcr DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Registries": [
            {
                "RegistryId": "tcr-xxx",
                "RegistryName": "test",
                "RegistryType": "basic",
                "Status": "running",
                "PublicDomain": "tcr-test.tencentcloudcr.com",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "RegionName": "ap-guangzhou",
                "RegionId": 1,
                "EnableAnonymous": true,
                "TokenValidTime": 1,
                "InternalEndpoint": "nil",
                "TagSpecification": {
                    "ResourceType": "abc",
                    "Tags": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ]
                },
                "ExpiredAt": "abc",
                "PayMod": 0,
                "RenewFlag": 0,
                "DeletionProtection": true
            }
        ],
        "RequestId": "abc"
    }
}
```

