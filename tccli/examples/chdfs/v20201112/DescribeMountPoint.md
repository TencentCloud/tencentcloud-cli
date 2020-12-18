**Example 1: 查看挂载点详细信息**

查看挂载点详细信息

Input: 

```
tccli chdfs DescribeMountPoint --cli-unfold-argument  \
    --MountPointId f4mnvilzmdd-Tx5f
```

Output: 
```
{
    "Response": {
        "MountPoint": {
            "MountPointId": "f4mnvilzmdd-Tx5f",
            "MountPointName": "test",
            "FileSystemId": "f4mnvilzmdd",
            "AccessGroupIds": [
                "ag-fmfpk1hk"
            ],
            "Status": 2,
            "CreateTime": "2019-07-30T18:19:18+08:00"
        },
        "RequestId": "9e0a4f46-e326-4e03-bc84-721008bb7a9d"
    }
}
```

