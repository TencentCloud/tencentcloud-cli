**Example 1: 查询登录配置**



Input: 

```
tccli tcb DescribeLoginConfig --cli-unfold-argument  \
    --EnvId env-123
```

Output: 
```
{
    "Response": {
        "AnonymousLogin": true,
        "EmailLogin": true,
        "MfaConfig": {
            "Email": "FALSE",
            "On": "TRUE",
            "RequiredBindPhone": "TRUE",
            "Sms": "TRUE"
        },
        "PhoneNumberLogin": true,
        "PwdUpdateStrategy": {
            "FirstLoginUpdate": true,
            "PeriodType": "MONTH",
            "PeriodUpdate": true,
            "PeriodValue": 6
        },
        "SmsVerificationConfig": {
            "Method": "",
            "Name": "",
            "SmsDayLimit": -1,
            "Type": "default"
        },
        "UserNameLogin": true,
        "RequestId": "9f69a66b-7302-4c00-b83a-04526851dd8f"
    }
}
```

