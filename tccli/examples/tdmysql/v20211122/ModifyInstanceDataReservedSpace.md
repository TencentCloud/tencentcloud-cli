**Example 1: ModifyInstanceDataReservedSpace用法**



Input: 

```
tccli tdmysql ModifyInstanceDataReservedSpace --cli-unfold-argument  \
    --InstanceId tdsql3-51780d0c \
    --ReservedSpaceGB 5
```

Output: 
```
{
    "Response": {
        "TaskId": 75267,
        "RequestId": "cbc2b9ef-676f-4c84-abdb-71753660fa80"
    }
}
```

