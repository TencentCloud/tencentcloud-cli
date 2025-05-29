**Example 1: 查询备份下载限制**

查询备份下载限制

Input: 

```
tccli cynosdb DescribeBackupDownloadRestriction --cli-unfold-argument  \
    --ClusterIds cynosdbmysql-2p3wjmzt
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

