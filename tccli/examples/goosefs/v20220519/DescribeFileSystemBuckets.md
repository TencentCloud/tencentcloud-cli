**Example 1: 罗列文件系统关联的Bucket映射**

罗列文件系统关联的Bucket映射

Input: 

```
tccli goosefs DescribeFileSystemBuckets --cli-unfold-argument  \
    --FileSystemId x_c60_r3c4fa1f
```

Output: 
```
{
    "Response": {
        "BucketList": [
            {
                "BucketName": "mybucket-12500000",
                "FileSystemPath": "/",
                "DataRepositoryTaskAutoStrategy": [
                    "AutoImportData",
                    "AutoImportMeta"
                ],
                "RuleId": "x-rule-1"
            },
            {
                "BucketName": "mytest-12500000",
                "FileSystemPath": "/aaa",
                "DataRepositoryTaskAutoStrategy": [
                    "OndemandImport",
                    "AutoImportMeta",
                    "PeriodExport"
                ],
                "RuleId": "x-rule-2"
            }
        ],
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

