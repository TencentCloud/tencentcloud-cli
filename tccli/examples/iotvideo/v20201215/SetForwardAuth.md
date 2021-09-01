**Example 1: 设置转发权限**



Input: 

```
tccli iotvideo SetForwardAuth --cli-unfold-argument  \
    --Skey xrnWgKu0fCz7q8JIQYFiNP-XpyaziljFvrQg4A*Cidc_ \
    --QueueType 1
```

Output: 
```
{
    "Response": {
        "ErrMsg": "",
        "RoleName": "ckafkaIoTCloud_QCSRole",
        "RoleID": 1724847,
        "RequestId": "6e85b1e5-6bbe-4731-8902-df7b6c308fda",
        "QueueType": 1,
        "Endpoint": "100011064235",
        "Result": 0
    }
}
```

