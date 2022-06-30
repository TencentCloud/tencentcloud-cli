**Example 1: 元数据锁检查**



Input: 

```
tccli dlc CheckLockMetaData --cli-unfold-argument  \
    --LockId 0 \
    --DatasourceConnectionName xx
```

Output: 
```
{
    "Response": {
        "LockId": 0,
        "LockState": "xx",
        "RequestId": "xx"
    }
}
```

