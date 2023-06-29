**Example 1: SendSms**



Input: 

```
tccli zj SendSms --cli-unfold-argument  \
    --License KA3431QZPU \
    --Phone +8613800138000 \
    --TemplateId bbb \
    --Sign 签名
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "SerialNo": "xxxxxx",
                "PhoneNumber": "+8613800138000",
                "Fee": 1,
                "Code": "Ok",
                "Message": "send success"
            }
        ],
        "RequestId": "xxxxx"
    }
}
```

**Example 2: zhuji-beta-paas-sendsms-20210914**



Input: 

```
tccli zj SendSms --cli-unfold-argument  \
    --Content  \
    --License KA3431QZPU \
    --SenderId  \
    --Sign 腾讯云珠玑 \
    --SmsType 1 \
    --Phone +8618956778559 \
    --TemplateId 1066724 \
    --International 0 \
    --SessionContext 123abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "SerialNo": "2645:258095476616315918736737855",
                "PhoneNumber": "+8618956778559",
                "Fee": 1,
                "Code": "Ok",
                "Message": "send success"
            }
        ],
        "RequestId": "dc0d77af-2f8f-4ed8-b582-4244120893d0"
    }
}
```

