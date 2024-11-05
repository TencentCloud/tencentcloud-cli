**Example 1: 查询资源包列表**

查询资源包列表


Input: 

```
tccli cynosdb DescribeResourcePackageList --cli-unfold-argument  \
    --PackageId package-bst68sh3 \
    --PackageName 自定义资源包名称-1 \
    --PackageType CCU \
    --PackageRegion chineseMainland \
    --Status using \
    --OrderBy createTime \
    --OrderDirection desc \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Total": 20,
        "Detail": [
            {
                "AppId": 12387234,
                "PackageId": "package-cbhsyegx",
                "PackageName": "MyPackageName",
                "PackageType": "CCU",
                "PackageRegion": "chineseMainland",
                "Status": "using",
                "PackageTotalSpec": 10000000,
                "PackageUsedSpec": 2394.3,
                "HasQuota": true,
                "BindInstanceInfos": [
                    {
                        "InstanceId": "cynosdbpg-ins-bzkxxrmt",
                        "InstanceRegion": "ap-guangzhou",
                        "InstanceType": "cynosdb-serverless"
                    }
                ],
                "StartTime": "2023-12-10 00:00:00",
                "ExpireTime": "2025-11-10 00:00:00"
            }
        ],
        "RequestId": "e0c28bb4-a0f2-4194-a646-b8bcf777b5ce"
    }
}
```

