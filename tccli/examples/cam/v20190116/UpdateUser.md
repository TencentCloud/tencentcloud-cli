**Example 1: 更新子用户**



Input: 

```
tccli cam UpdateUser --cli-unfold-argument  \
    --Remark test \
    --Name test124 \
    --CountryCode 86 \
    --NeedResetPassword 0 \
    --PhoneNum 10086 \
    --ConsoleLogin 1 \
    --Password test123456 \
    --Email 123%40qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

