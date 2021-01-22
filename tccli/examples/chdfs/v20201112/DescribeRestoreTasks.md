**Example 1: 查看回热任务列表**

查看回热任务列表

Input: 

```
tccli chdfs DescribeRestoreTasks --cli-unfold-argument  \
    --FileSystemId f4mnvilzmdd
```

Output: 
```
{
    "Response": {
        "RestoreTasks": [
            {
                "RestoreTaskId": 1,
                "FilePath": "/test/file1",
                "Type": 1,
                "Days": 7,
                "Status": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            },
            {
                "RestoreTaskId": 2,
                "FilePath": "/test/file2",
                "Type": 2,
                "Days": 7,
                "Status": 2,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            }
        ],
        "RequestId": "19d240f4-156d-4a3c-856c-216d64a6bb4a"
    }
}
```

