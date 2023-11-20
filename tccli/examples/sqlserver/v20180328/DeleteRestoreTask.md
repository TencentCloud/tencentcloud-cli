**Example 1: 删除回档任务记录**

删除回档任务记录

Input: 

```
tccli sqlserver DeleteRestoreTask --cli-unfold-argument  \
    --InstanceId mssql-jsuij219 \
    --RestoreIds 0
```

Output: 
```
{
    "Response": {
        "RequestId": "863b2797-858b-49f3-88e9-50159e564cbc"
    }
}
```

