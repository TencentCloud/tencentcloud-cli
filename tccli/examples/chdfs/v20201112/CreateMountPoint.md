**Example 1: 创建挂载点**

创建挂载点

Input: 

```
tccli chdfs CreateMountPoint --cli-unfold-argument  \
    --MountPointName test \
    --FileSystemId f4mnvilzmdd \
    --MountPointStatus 1
```

Output: 
```
{
    "Response": {
        "MountPoint": {
            "MountPointId": "f4mnvilzmdd-Tx5f",
            "MountPointName": "test",
            "FileSystemId": "f4mnvilzmdd",
            "AccessGroupIds": [],
            "Status": 1,
            "CreateTime": "2019-07-30T18:19:18+08:00"
        },
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

