**Example 1: 请求demo**



Input: 

```
tccli wedata AcquireLock --cli-unfold-argument  \
    --ProjectId 123 \
    --ResourcePath ds:test.sh \
    --ResourceType TASK
```

Output: 
```
{
    "Response": {
        "RequestId": "111",
        "LockerId": 222,
        "LockerName": "222",
        "LockedByMe": true,
        "EditFlag": true,
        "ResourcePath": "aaaa",
        "LockTime": 1647238779956
    }
}
```

**Example 2: 成功获取锁**



Input: 

```
tccli wedata AcquireLock --cli-unfold-argument  \
    --ResourcePath 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "2002c55b-4b70-461a-9a29-549483c06810",
        "LockerId": 100022256608,
        "LockerName": "fe",
        "ResourcePath": "字符串",
        "EditFlag": true,
        "LockedByMe": true,
        "LockTime": 1647346191208
    }
}
```

**Example 3: 成功获取资源锁**



Input: 

```
tccli wedata AcquireLock --cli-unfold-argument  \
    --ResourcePath 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "f55cf080-ecc3-4106-976b-9211c6a75070",
        "LockerId": 100022256608,
        "LockerName": "fe",
        "ResourcePath": "字符串",
        "EditFlag": true,
        "LockedByMe": true,
        "LockTime": 1647422951982
    }
}
```

