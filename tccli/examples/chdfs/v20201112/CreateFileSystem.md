**Example 1: 创建文件系统**

创建文件系统

Input: 

```
tccli chdfs CreateFileSystem --cli-unfold-argument  \
    --FileSystemName fs-test \
    --PosixAcl True \
    --Description create an example fs \
    --CapacityQuota 1073741824
```

Output: 
```
{
    "Response": {
        "FileSystem": {
            "AppId": 1251660000,
            "BlockSize": 4194304,
            "CapacityQuota": 1073741824,
            "CreateTime": "2024-12-24T20:12:43+08:00",
            "Description": "create an example fs",
            "EnableRanger": false,
            "FileSystemId": "f14mrrxxxxxx",
            "FileSystemName": "fs-test",
            "PosixAcl": true,
            "RangerServiceAddresses": [],
            "Region": "ap-guangzhou",
            "Status": 1,
            "SuperUsers": []
        },
        "RequestId": "63b54170-aca3-410b-8e24-2e42dbfa83e1"
    }
}
```

