**Example 1: 修改基础备份过期时间**

修改实例postgres-9n26zs6n下基础备份集88d3a71e-b822-5728-9d41-d8cfc0d0556e的过期时间为“2023-02-18 23:59:59”。

Input: 

```
tccli postgres ModifyBaseBackupExpireTime --cli-unfold-argument  \
    --BaseBackupId 88d3a71e-b822-5728-9d41-d8cfc0d0556e \
    --DBInstanceId postgres-9n26zs6n \
    --NewExpireTime 2023-02-18 23:59:59
```

Output: 
```
{
    "Response": {
        "RequestId": "be3bafde-f34e-4fda-9f40-04c5515e2148"
    }
}
```

