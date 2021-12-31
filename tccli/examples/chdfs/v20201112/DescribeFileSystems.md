**Example 1: 查看文件系统列表**

查看文件系统列表

Input: 

```
tccli chdfs DescribeFileSystems --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FileSystems": [
            {
                "AppId": 1251006373,
                "FileSystemName": "test",
                "Description": "",
                "Region": "ap-guangzhou",
                "FileSystemId": "f4mnvilzmdd",
                "CreateTime": "2019-07-30T17:03:20+08:00",
                "BlockSize": 4194304,
                "CapacityQuota": 1073741824,
                "SuperUsers": [
                    "hadoop"
                ],
                "PosixAcl": true,
                "Status": 2,
                "EnableRanger": false,
                "RangerServiceAddresses": [
                    "127.0.0.1:8080"
                ]
            }
        ],
        "RequestId": "a6d1c90a-a86a-45e2-b031-0de50f1ffc35"
    }
}
```

