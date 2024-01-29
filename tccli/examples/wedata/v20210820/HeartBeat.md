**Example 1: 请求demo**



Input: 

```
tccli wedata HeartBeat --cli-unfold-argument  \
    --ResourcePath ds:test.sh \
    --EditFlag True
```

Output: 
```
{
    "Response": {
        "RequestId": 111,
        "LockerId": 222,
        "LockerName": "222",
        "StealFlag": false,
        "LockedByMe": true,
        "Locked": true,
        "EditFlag": true,
        "ResourcePath": "aaaa",
        "LockTime": 1647238779956
    }
}
```

**Example 2: 心跳成功**



Input: 

```
tccli wedata HeartBeat --cli-unfold-argument  \
    --EditFlag true \
    --ResourcePath 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "e995d171-f273-45c9-bb73-9c51ca49d2f0",
        "LockerId": 100022256608,
        "LockerName": "fe",
        "StealFlag": false,
        "LockedByMe": true,
        "Locked": true,
        "EditFlag": true,
        "ResourcePath": "字符串",
        "LockTime": 1647346134723
    }
}
```

