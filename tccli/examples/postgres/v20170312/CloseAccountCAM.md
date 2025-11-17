**Example 1: 关闭数据库账号的cam验证**



Input: 

```
tccli postgres CloseAccountCAM --cli-unfold-argument  \
    --DBInstanceId postgres-r95q23pn \
    --UserName root \
    --Password 1359Qwe! \
    --PasswordEncrypt False
```

Output: 
```
{
    "Response": {
        "RequestId": "12cc9ebc-6fc1-4f24-9ff2-5695c10e125d"
    }
}
```

