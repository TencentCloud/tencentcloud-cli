**Example 1: 查看回收站配置**

查看回收站配置

Input: 

```
tccli chdfs DescribeTrashConfig --cli-unfold-argument  \
    --FileSystemId f4mnvilzmdd
```

Output: 
```
{
    "Response": {
        "TrashConfig": {
            "FileSystemId": "f4mnvilzmdd",
            "ReservedDays": 1,
            "Path": "/e88dea7e_trash",
            "Status": 1
        },
        "RequestId": "19d240f4-156d-4a3c-856c-216d64a6bb4a"
    }
}
```

