**Example 1: 元数据锁检查**



Input: 

```
tccli dlc CheckLockMetaData --cli-unfold-argument  \
    --LockId 1 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "LockId": 1,
        "LockState": "ACQUIRED",
        "RequestId": "********-****-****-****-842f5f01a127"
    }
}
```

