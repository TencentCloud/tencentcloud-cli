**Example 1: 创建数据库普通账号**

创建数据库普通账号

Input: 

```
tccli postgres CreateAccount --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName user_normal \
    --Password Test_password1 \
    --Type normal \
    --Remark 
```

Output: 
```
{
    "Response": {
        "RequestId": "5d19322f-50fe-4084-a5d3-b0bc680fd3a1"
    }
}
```

**Example 2: 创建数据库超级账号**

创建数据库超级账号


Input: 

```
tccli postgres CreateAccount --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName user_Super \
    --Password Test_password1 \
    --Type tencentDBSuper \
    --Remark 超级用户
```

Output: 
```
{
    "Response": {
        "RequestId": "fad9ac43-c906-4494-bbb5-88d154d2829c"
    }
}
```

