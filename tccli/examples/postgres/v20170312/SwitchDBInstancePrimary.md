**Example 1: 切换实例主备关系**

切换实例postgres-idabksrn的主备关系，采用非强制切换，并立即切换

Input: 

```
tccli postgres SwitchDBInstancePrimary --cli-unfold-argument  \
    --DBInstanceId postgres-idabksrn
```

Output: 
```
{
    "Response": {
        "RequestId": "54eeac1a-1d21-43d9-8293-1352d5874860"
    }
}
```

