**Example 1: 创建子用户**



Input: 

```
tccli cam AddUser --cli-unfold-argument  \
    --Name c***** \
    --PhoneNum 132*****828 \
    --CountryCode 86 \
    --Email gavinh************t.com
```

Output: 
```
{
    "Response": {
        "Name": "c*****",
        "Password": "",
        "PhoneNumVerifyLink": "https://cloud.tencent.com/cam/verifyPhone?token=81bf4ca3537447af****************",
        "SecretId": "",
        "SecretKey": "",
        "Uid": 900000000,
        "Uin": 700003000000,
        "RequestId": "bfbeba3a-40a2-4eb9-b760-3fdf2c92170f"
    }
}
```

