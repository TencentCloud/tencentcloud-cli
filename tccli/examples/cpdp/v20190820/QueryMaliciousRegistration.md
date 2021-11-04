**Example 1: QueryMaliciousRegistration**



Input: 

```
tccli cpdp QueryMaliciousRegistration --cli-unfold-argument  \
    --MerchantId 1927856182 \
    --MerchantName 鹅厂公仔 \
    --CompanyName 深圳市南山有限公司 \
    --USCI 123456789 \
    --RegNumber 123456789 \
    --RegAddress 深圳市南山区粤海街道 \
    --RegTime 1632277247 \
    --EncryptedPhoneNumber 4C011539DDEAEBA5A7CF8EDFC18A9 \
    --EncryptedEmailAddress 2ff15aa732dd618090b2c78e0bb0e5 \
    --EncryptedPersonId 202cb92ac5907964b07152d234b70 \
    --Ip 127.0.0.1 \
    --Channel CH001
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "Result": {
            "RiskLevel": 0,
            "RiskTypes": "G001|T002"
        },
        "ErrMsg": "成功",
        "RequestId": "123"
    }
}
```

