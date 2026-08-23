**Example 1: 修改TCB实例账号密码**



Input: 

```
tccli postgres ResetTCBAccountPassword --cli-unfold-argument  \
    --DBInstanceId postgres-b1xd9rpr \
    --UserName cloudbase_postgres_test \
    --Password Fucker28.
```

Output: 
```
{
    "Response": {
        "RequestId": "cfc792bc-79b2-4377-9bcc-9634ae12ca2e"
    }
}
```

