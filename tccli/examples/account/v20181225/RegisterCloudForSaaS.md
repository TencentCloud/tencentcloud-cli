**Example 1: 注册SaaS用户**



Input: 

```
tccli account RegisterCloudForSaaS --cli-unfold-argument  \
    --ClientUA chrome \
    --ClientIP 1.1.1.1 \
    --CountryName CN \
    --CountryCode 86 \
    --RegisterType phone \
    --Lang zh \
    --Area 1 \
    --Platform co****g \
    --AccessLevel 3 \
    --PhoneNumber 132****9791 \
    --PhoneVerifyCode 42***43 \
    --Password 123***abcd
```

Output: 
```
{
    "Response": {
        "Uin": 300000000001,
        "Key": "d5c50bdcdb2****7b479b4f17bf5461e",
        "ExpiredTime": 1596875744,
        "RequestId": "e0e551ca-f2c1-4734-831a-3d677df0320c"
    }
}
```

