**Example 1: 查看文件系统详细信息**

查看文件系统详细信息

Input: 

```
tccli chdfs DescribeFileSystem --cli-unfold-argument  \
    --FileSystemId f4mhaqkciq0
```

Output: 
```
{
    "Response": {
        "FileSystem": {
            "AppId": 1251006373,
            "FileSystemName": "test",
            "Description": "",
            "Region": "ap-guangzhou",
            "FileSystemId": "f4mhaqkciq0",
            "CreateTime": "2019-07-30T17:03:20+08:00",
            "BlockSize": 4194304,
            "CapacityQuota": 1073741824,
            "Status": 2
        },
        "CapacityUsed": 0,
        "ArchiveCapacityUsed": 0,
        "RequestId": "22e36f95-9295-4132-a75e-09a08d2e13fc"
    }
}
```

