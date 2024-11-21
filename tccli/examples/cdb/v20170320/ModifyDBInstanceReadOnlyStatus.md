**Example 1: 设置MySQL云数据库实例为只读**



Input: 

```
tccli cdb ModifyDBInstanceReadOnlyStatus --cli-unfold-argument  \
    --InstanceId cdb-uns231ns \
    --ReadOnly 0
```

Output: 
```
{
    "Response": {
        "RequestId": "2cf0e063-0f70f622-2d5c3f7c-0e612ab0"
    }
}
```

