**Example 1: 获取防火墙同步状态**

获取防火墙同步状态，一般在执行同步操作后查询

Input: 

```
tccli cfw DescribeFwSyncStatus --cli-unfold-argument  \
    --SyncType abc
```

Output: 
```
{
    "Response": {
        "SyncStatus": 0,
        "RequestId": "abc"
    }
}
```

