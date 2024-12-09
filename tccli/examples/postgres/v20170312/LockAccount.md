**Example 1: 锁定数据库账号**

锁定数据库账号

Input: 

```
tccli postgres LockAccount --cli-unfold-argument  \
    --DBInstanceId postgres-4sfuv15b \
    --UserName app_user
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90"
    }
}
```

