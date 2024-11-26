**Example 1: 查询文件系统配额**



Input: 

```
tccli cfs DescribeUserQuota --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "UserQuotaInfo": [
            {
                "UserType": "Uid",
                "UserId": "1000",
                "FileSystemId": "cfs-12345",
                "CapacityHardLimit": 10,
                "FileHardLimit": 10000,
                "Status": "available",
                "DirectoryPath": "abc",
                "CapacityUsed": 1,
                "FileUsed": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81"
    }
}
```

