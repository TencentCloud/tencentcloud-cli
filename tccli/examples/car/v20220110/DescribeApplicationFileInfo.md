**Example 1: 添加查询应用文件信息请求**



Input: 

```
tccli car DescribeApplicationFileInfo --cli-unfold-argument  \
    --ApplicationId app-dafe32hr \
    --FilePathList xxx/file1.exe
```

Output: 
```
{
    "Response": {
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022",
        "FileInfoList": [
            {
                "FilePath": "xxx/file1.exe",
                "FileState": "EXIST"
            }
        ]
    }
}
```

