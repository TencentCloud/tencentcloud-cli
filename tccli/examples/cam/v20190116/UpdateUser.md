**Example 1: 更新子用户**



Input: 

```
tccli cam UpdateUser --cli-unfold-argument  \
    --Remark 财务管理 \
    --Name jack \
    --CountryCode 86 \
    --NeedResetPassword 0 \
    --PhoneNum 132*******86 \
    --ConsoleLogin 1 \
    --Password 2sd82*****ddw832je \
    --Email 3729*****qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

