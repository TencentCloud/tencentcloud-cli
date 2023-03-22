**Example 1: 添加子用户**

创建子账号

Input: 

```
tccli cam AddUser --cli-unfold-argument  \
    --Remark test \
    --Name test124 \
    --CountryCode 86 \
    --NeedResetPassword 0 \
    --PhoneNum 10086 \
    --UseApi 1 \
    --ConsoleLogin 1 \
    --Password test123456 \
    --Email 123%40qq.com
```

Output: 
```
{
    "Response": {
        "Uid": 5648765,
        "Uin": 100000546533,
        "Name": "test124",
        "Password": "test123456",
        "SecretId": "faweffewagwaegawe",
        "SecretKey": "fawef23rjhiuaefhuaifhiuawef",
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

