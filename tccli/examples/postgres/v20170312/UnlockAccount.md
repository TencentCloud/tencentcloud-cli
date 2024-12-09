**Example 1: 解除数据库账号锁定**

账号锁定之后，通过此操作解锁。

Input: 

```
tccli postgres UnlockAccount --cli-unfold-argument  \
    --DBInstanceId postgres-4sfuv15b \
    --UserName bob_admin
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90"
    }
}
```

