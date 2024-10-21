**Example 1: 获取防火墙路由同步状态**

获取防火墙路由同步状态

Input: 

```
tccli cfw DescribeFwSyncStatus --cli-unfold-argument  \
    --SyncType Route
```

Output: 
```
{
    "Response": {
        "RequestId": "00075104-8d9e-4b29-a0b1-b0609a4ce726",
        "SyncStatus": 0
    }
}
```

