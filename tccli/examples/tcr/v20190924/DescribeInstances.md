**Example 1: 查看实例列表**



Input: 

```
tccli tcr DescribeInstances --cli-unfold-argument  \
    --Registryids tcr-dg284imq
```

Output: 
```
{
    "Response": {
        "Registries": [
            {
                "CreatedAt": "2024-07-19T15:33:22+08:00",
                "DeletionProtection": true,
                "EnableAnonymous": true,
                "ExpiredAt": "",
                "InternalEndpoint": "10.1.66.46",
                "PayMod": 0,
                "PublicDomain": "nicokang-tcr-gz.tencentcloudcr.com",
                "RegionId": 1,
                "RegionName": "ap-guangzhou",
                "RegistryId": "tcr-dg284imq",
                "RegistryName": "nicokang-tcr-gz",
                "RegistryType": "premium",
                "RenewFlag": 0,
                "Status": "Running",
                "TagSpecification": {
                    "ResourceType": "instance",
                    "Tags": [
                        {
                            "Key": "tcr-test2",
                            "Value": "ericyyyang2"
                        },
                        {
                            "Key": "tcr-test",
                            "Value": "nicokang"
                        }
                    ]
                },
                "TokenValidTime": 87600
            }
        ],
        "RequestId": "06d6c73a-d845-4e20-a578-721a0cf7e268",
        "TotalCount": 1
    }
}
```

