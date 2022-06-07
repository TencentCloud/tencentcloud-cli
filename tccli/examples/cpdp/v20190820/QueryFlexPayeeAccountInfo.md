**Example 1: 收款用户账户信息查询**



Input: 

```
tccli cpdp QueryFlexPayeeAccountInfo --cli-unfold-argument  \
    --PayeeId 1529657731805986816 \
    --OutUserId test123123213
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "AccountId": "AC615499841879322625",
            "AccountName": "account0526105637",
            "Remark": null,
            "CreateTime": "2022-05-26 10:56:37",
            "UserInfo": {
                "OutUserId": "0526105637test",
                "UserType": 1,
                "IdType": 0,
                "IdNo": "610113192105041627",
                "Name": "张三"
            },
            "PropertyInfo": {
                "SettleRightStatus": "ENABLE",
                "PaymentRightStatus": "ENABLE"
            }
        },
        "RequestId": "8b4aee61-a20a-4135-96e1-144596a7e3bc"
    }
}
```

