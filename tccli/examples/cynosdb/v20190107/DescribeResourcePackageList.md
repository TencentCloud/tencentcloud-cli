**Example 1: 查询资源包列表**

查询资源包列表


Input: 

```
tccli cynosdb DescribeResourcePackageList --cli-unfold-argument  \
    --PackageId package-abcd1234 \
    --PackageName 自定义资源包名称-1 \
    --PackageType CCU \
    --PackageRegion china \
    --Status using \
    --OrderBy createTime \
    --OrderDirection desc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Detail": [
            {
                "AppId": 0,
                "PackageId": "abc",
                "PackageName": "abc",
                "PackageType": "abc",
                "PackageRegion": "abc",
                "Status": "abc",
                "PackageTotalSpec": 0,
                "PackageUsedSpec": 0,
                "HasQuota": true,
                "BindInstanceInfos": [
                    {
                        "InstanceId": "abc",
                        "InstanceRegion": "abc",
                        "InstanceType": "abc"
                    }
                ],
                "StartTime": "abc",
                "ExpireTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

