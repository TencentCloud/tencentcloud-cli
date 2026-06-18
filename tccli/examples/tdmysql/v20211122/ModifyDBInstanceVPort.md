**Example 1: 修改端口**



Input: 

```
tccli tdmysql ModifyDBInstanceVPort --cli-unfold-argument  \
    --InstanceId tdsql3-f192ab1c \
    --Vport 3306
```

Output: 
```
{
    "Response": {
        "FlowId": 111,
        "RequestId": "84280be1-7a55-4ec9-ab41-ddfc9aaf7ad9"
    }
}
```

