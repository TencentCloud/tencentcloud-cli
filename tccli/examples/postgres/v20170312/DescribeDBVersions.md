**Example 1: 查询版本号列表**

新购实例、升级实例版本号时，可通过此接口查询有效的数据库版本号列表

Input: 

```
tccli postgres DescribeDBVersions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "99fd1cde-d477-4cb4-8a05-12b62502e6fc",
        "VersionSet": [
            {
                "AvailableUpgradeTarget": [],
                "DBEngine": "mssql_compatible",
                "DBKernelVersion": "v14.3_r1.3",
                "DBMajorVersion": "14",
                "DBVersion": "14.3",
                "Status": "AVAILABLE",
                "SupportedFeatureNames": []
            },
            {
                "AvailableUpgradeTarget": [
                    "v14.3_r1.3"
                ],
                "DBEngine": "postgresql",
                "DBKernelVersion": "v14.2_r1.1",
                "DBMajorVersion": "14",
                "DBVersion": "14.2",
                "Status": "AVAILABLE",
                "SupportedFeatureNames": [
                    "TDE"
                ]
            },
            {
                "AvailableUpgradeTarget": [
                    "v14.3_r1.3",
                    "v14.2_r1.1"
                ],
                "DBEngine": "postgresql",
                "DBKernelVersion": "v14.2_r1.0",
                "DBMajorVersion": "14",
                "DBVersion": "14.2",
                "Status": "AVAILABLE",
                "SupportedFeatureNames": [
                    "TDE"
                ]
            }
        ]
    }
}
```

