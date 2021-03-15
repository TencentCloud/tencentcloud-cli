**Example 1: 杀死指定会话**



Input: 

```
tccli mariadb KillSession --cli-unfold-argument  \
    --InstanceId tdsql-2gk4nxyz \
    --SessionId 1111 2222
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "TaskId": 11
    }
}
```

