**Example 1: 发送短信息接口**



Input: 

```
tccli ic SendSms --cli-unfold-argument  \
    --Sdkappid 1200168178 \
    --Iccid 89860619000013360957 \
    --Content openok
```

Output: 
```
{
    "Response": {
        "RequestId": "124145i30913",
        "Data": {
            "Iccid": "89860619000013360957",
            "Sid": "15512545038707740006873886999"
        }
    }
}
```

