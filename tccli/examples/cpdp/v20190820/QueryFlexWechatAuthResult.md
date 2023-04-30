**Example 1: 微工卡预核身结果查询**

微工卡预核身结果查询

Input: 

```
tccli cpdp QueryFlexWechatAuthResult --cli-unfold-argument  \
    --AuthNo abc
```

Output: 
```
{
    "Response": {
        "ErrCode": "abc",
        "ErrMessage": "abc",
        "Result": {
            "AuthNo": "abc",
            "OpenId": "abc",
            "MchId": "abc",
            "SubMchId": "abc",
            "AuthScene": "abc",
            "AuthSource": "abc",
            "ProjectName": "abc",
            "EmployerName": "abc",
            "AuthTime": "abc",
            "AuthType": "abc",
            "AuthState": "abc",
            "AuthFailReason": "abc"
        },
        "RequestId": "abc"
    }
}
```

