**Example 1: 查询实例版本属性**



Input: 

```
tccli cdb DescribeDBFeatures --cli-unfold-argument  \
    --InstanceId cdb-qwerasdf
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "IsSupportAudit": true,
        "AuditNeedUpgrade": false,
        "IsSupportEncryption": true,
        "EncryptionNeedUpgrade": false,
        "IsRemoteRo": false,
        "MasterRegion": "",
        "IsSupportUpdateSubVersion": true,
        "CurrentSubVersion": "20190203",
        "TargetSubVersion": "20190930"
    }
}
```

