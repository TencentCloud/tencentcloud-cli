**Example 1: 批量发送短信成功示例**

批量发送短信成功。

Input: 

```
tccli sms SendMultiGlobalSms --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --MultiSmsInfoSet.0.PhoneNumber +60198***000 \
    --MultiSmsInfoSet.0.TemplateId 1800308 \
    --MultiSmsInfoSet.0.TemplateParamSet 190191 \
    --MultiSmsInfoSet.0.SenderId Qsms \
    --MultiSmsInfoSet.0.SessionContext outsid_1776313405_1001 \
    --MultiSmsInfoSet.1.PhoneNumber +60198***001 \
    --MultiSmsInfoSet.1.TemplateId 1800308 \
    --MultiSmsInfoSet.1.TemplateParamSet 190192 \
    --MultiSmsInfoSet.1.SenderId Qsms \
    --MultiSmsInfoSet.1.SessionContext outsid_1776313405_1002
```

Output: 
```
{
    "Response": {
        "SendMultiStatusSet": [
            {
                "Code": "Ok",
                "Fee": 1,
                "IsoCode": "MY",
                "Message": "send success",
                "PhoneNumber": "+60198***000",
                "SerialNo": "a84166ff-8c6c-41f7-923b-9fdd27fd0fe4",
                "SessionContext": "outsid_1776313405_1001"
            },
            {
                "Code": "Ok",
                "Fee": 1,
                "IsoCode": "MY",
                "Message": "send success",
                "PhoneNumber": "+60198***001",
                "SerialNo": "72f1f018-a0c8-4101-976b-265f25b4c0a2",
                "SessionContext": "outsid_1776313405_1002"
            }
        ],
        "RequestId": "104cc55c-05f1-456c-8a0b-18cf25ef56a4"
    }
}
```

**Example 2: 批量发送短信失败示例**

批量发送短信失败。

Input: 

```
tccli sms SendMultiGlobalSms --cli-unfold-argument  \
    --SmsSdkAppId 1400006666 \
    --MultiSmsInfoSet.0.PhoneNumber +60198***000 \
    --MultiSmsInfoSet.0.TemplateId 1800308 \
    --MultiSmsInfoSet.0.SenderId Qsms \
    --MultiSmsInfoSet.0.SessionContext outsid_1776313405_1001 \
    --MultiSmsInfoSet.1.PhoneNumber +60198***001 \
    --MultiSmsInfoSet.1.TemplateId 1800308 \
    --MultiSmsInfoSet.1.SenderId Qsms \
    --MultiSmsInfoSet.1.SessionContext outsid_1776313405_1002
```

Output: 
```
{
    "Response": {
        "SendMultiStatusSet": [
            {
                "Code": "FailedOperation.TemplateIncorrectOrUnapproved",
                "Fee": 0,
                "IsoCode": "MY",
                "Message": "template is not approved or request content does not match the approved template content",
                "PhoneNumber": "+60198***000",
                "SerialNo": "de61cf79-636e-4ad0-ac0b-dc29937999af",
                "SessionContext": "outsid_1776313405_1001"
            },
            {
                "Code": "FailedOperation.TemplateIncorrectOrUnapproved",
                "Fee": 0,
                "IsoCode": "MY",
                "Message": "template is not approved or request content does not match the approved template content",
                "PhoneNumber": "+60198***001",
                "SerialNo": "0b8780c6-e889-4201-87fb-5e8e282b3b3e",
                "SessionContext": "outsid_1776313405_1002"
            }
        ],
        "RequestId": "4899adba-08e2-4350-9fee-ab37b7560c4c"
    }
}
```

