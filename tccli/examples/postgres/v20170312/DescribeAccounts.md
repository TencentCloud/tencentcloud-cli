**Example 1: 获取实例postgres-hpe52jnz的账户列表**

获取实例postgres-hpe52jnz的账户列表

Input: 

```
tccli postgres DescribeAccounts --cli-unfold-argument  \
    --DBInstanceId postgres-hpe52jnz
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CreateTime": "2024-05-06 21:00:12",
                "DBInstanceId": "postgres-hpe52jnz",
                "Remark": "",
                "Status": 2,
                "UpdateTime": "2024-06-06 21:00:12",
                "UserName": "app_user",
                "UserType": "tencentDBSuper"
            }
        ],
        "RequestId": "1299fe3a-9958-440a-bfd0-e4eb1e71b7eb",
        "TotalCount": 1
    }
}
```

