**Example 1: 查询实例版本属性**

查询实例特性，诸如内核小版本、是否开启审计等。

Input: 

```
tccli cdb DescribeDBFeatures --cli-unfold-argument  \
    --InstanceId cdb-qwerasdf
```

Output: 
```
{
    "Response": {
        "AuditNeedUpgrade": false,
        "CurrentSubVersion": "20230701",
        "EncryptionNeedUpgrade": false,
        "IsRemoteRo": false,
        "IsSupportAudit": true,
        "IsSupportEncryption": true,
        "IsSupportUpdateSubVersion": true,
        "MasterRegion": "",
        "RequestId": "68782c1e-d613-4451-b993-adef1cc7a3a6",
        "TargetSubVersion": "20230702"
    }
}
```

