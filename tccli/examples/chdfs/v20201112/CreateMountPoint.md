**Example 1: 创建挂载点**

创建挂载点

Input: 

```
tccli chdfs CreateMountPoint --cli-unfold-argument  \
    --MountPointName mp-test \
    --FileSystemId f14mrrxxxxxx \
    --MountPointStatus 1
```

Output: 
```
{
    "Response": {
        "MountPoint": {
            "AccessGroupIds": [],
            "CreateTime": "2024-12-25T19:15:28+08:00",
            "FileSystemId": "f14mrrxxxxxx",
            "MountPointId": "f14mrrxxxxxx-C1Yv",
            "MountPointName": "mp-test",
            "Status": 1
        },
        "RequestId": "a7474fac-2e8d-456f-8283-9def4c0ff559"
    }
}
```

