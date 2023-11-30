**Example 1: 开启\关闭\更新SSL加密**

开启\关闭\更新SSL加密

Input: 

```
tccli sqlserver ModifyDBInstanceSSL --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --Type enable \
    --WaitSwitch 0
```

Output: 
```
{
    "Response": {
        "FlowId": 100001,
        "RequestId": "9db13c19-d660-43c4-b340-7ba86b7b1470"
    }
}
```

