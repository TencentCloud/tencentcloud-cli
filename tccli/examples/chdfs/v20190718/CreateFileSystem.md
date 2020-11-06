**Example 1: 创建文件系统**

创建文件系统

Input: 

```
tccli chdfs CreateFileSystem --cli-unfold-argument  \
    --FileSystemName test \
    --Description test \
    --CapacityQuota 1073741824
```

Output: 
```
{
    "Response": {
        "FileSystem": {
            "AppId": 1251006373,
            "FileSystemName": "test",
            "Description": "test",
            "Region": "ap-guangzhou",
            "FileSystemId": "f4mhaqkciq0",
            "CreateTime": "2019-07-30T16:51:41+08:00",
            "BlockSize": 4194304,
            "CapacityQuota": 1073741824,
            "Status": 1
        },
        "RequestId": "ecba2ede-de08-41d5-99cc-b5444912b7f2"
    }
}
```

