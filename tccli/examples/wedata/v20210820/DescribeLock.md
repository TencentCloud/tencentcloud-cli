**Example 1: 查询数据开发资源锁状态**

查询数据开发资源锁状态

Input: 

```
tccli wedata DescribeLock --cli-unfold-argument  \
    --ResourcePath abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "LockerId": 1,
            "LockerName": "abc",
            "ResourcePath": "abc",
            "LockedByMe": true,
            "LockTime": 1
        },
        "RequestId": "abc"
    }
}
```

