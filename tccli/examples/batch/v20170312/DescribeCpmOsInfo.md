**Example 1: 查询批量计算黑石操作系统信息**



Input: 

```
tccli batch DescribeCpmOsInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "OsInfoSet": [
            {
                "OsEnglishDescription": "Windows Server 2012 datacenter cn 64bit",
                "OsName": "BM-XServer_V12cdb_x64",
                "MaxPartitionSize": 1000000,
                "ImageTag": "public",
                "OsTypeId": 125,
                "OsDescription": "Windows Server 2012 数据中心中文版 batch",
                "OsClass": "Windows"
            },
            {
                "OsEnglishDescription": "Centos 7.3 64bit",
                "OsName": "BM-centos7.3",
                "MaxPartitionSize": 50,
                "ImageTag": "public",
                "OsTypeId": 47,
                "OsDescription": "Centos 7.3 64位",
                "OsClass": "CentOS"
            },
            {
                "OsEnglishDescription": "Centos 6.8 64bit",
                "OsName": "BM-centos6.8",
                "MaxPartitionSize": 16,
                "ImageTag": "public",
                "OsTypeId": 48,
                "OsDescription": "Centos 6.8 64位",
                "OsClass": "CentOS"
            },
            {
                "OsEnglishDescription": "Centos 6.5 64bit",
                "OsName": "BM-centos6.5",
                "MaxPartitionSize": 16,
                "ImageTag": "public",
                "OsTypeId": 1,
                "OsDescription": "Centos 6.5  64位",
                "OsClass": "CentOS"
            },
            {
                "OsEnglishDescription": "Centos 7.2  64bit",
                "OsName": "BM-centos7.2",
                "MaxPartitionSize": 50,
                "ImageTag": "public",
                "OsTypeId": 2,
                "OsDescription": "Centos 7.2  64位",
                "OsClass": "CentOS"
            }
        ],
        "RequestId": "b53f11cc-8583-4533-8bec-686ca56799eb"
    }
}
```

