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

