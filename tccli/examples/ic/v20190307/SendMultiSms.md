**Example 1: 群发短信**



Input: 

```
tccli ic SendMultiSms --cli-unfold-argument  \
    --Sdkappid 1200168178 \
    --Iccids ["89860619000013360957","89860619000013360957"] \
    --Content ok
```

Output: 
```
{
    "Response": {
        "RequestId": "124145i30913",
        "Data": [
            {
                "Code": "0",
                "Msg": "成功",
                "Iccid": "89860619000013360940",
                "Sid": "15512560992520710006873885999"
            },
            {
                "Code": "0",
                "Msg": "成功",
                "Iccid": "89860619000013360957",
                "Sid": "15512560992520830006873886999"
            }
        ]
    }
}
```

