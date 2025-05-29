**Example 1: 当前地域用户级别设置的默认备份下载来源限制**

当前地域用户级别设置的默认备份下载来源限制

Input: 

```
tccli cynosdb DescribeBackupDownloadUserRestriction --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --OnlyUserRestriction False
```

Output: 
```
{
    "Response": {
        "BackupLimitClusterRestrictions": [
            {
                "BackupLimitRestriction": {
                    "IpComparisonSymbol": "In",
                    "LimitIps": [],
                    "LimitType": "Customize",
                    "LimitVpcs": [
                        {
                            "Region": "ap-guangzhou",
                            "VpcList": []
                        }
                    ],
                    "VpcComparisonSymbol": "In"
                },
                "ClusterId": "cynosdbmysql-2p3wjmzt"
            }
        ],
        "RequestId": "36eca298-c9b7-4e13-8f33-3c07926ee0d8"
    }
}
```

