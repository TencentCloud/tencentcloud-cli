**Example 1: ExportResourcePackageDeductDetails**

资源包使用明细导出

Input: 

```
tccli cynosdb ExportResourcePackageDeductDetails --cli-unfold-argument  \
    --PackageId package-abcd1234 \
    --ClusterIds cynosdbmysql-bcdz3214 \
    --OrderBy createTime \
    --OrderByType desc \
    --StartTime 2022-01-01 01:01:01 \
    --EndTime 2024-01-01 01:01:01 \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "FileContent": "2022-01-01 01:01:01,package-abcd1234,200.00,1298.98,cynosdbmysql-cdba4312\n2022-01-01 01:02:01,package-abcd1234,200.00,1498.98,cynosdbmysql-cdba4354",
        "RequestId": "abc"
    }
}
```

