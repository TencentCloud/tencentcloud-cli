**Example 1: 查询报名表单数据**



Input: 

```
tccli opc GetActivityRegFormRecordList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 1 \
    --ActivityId 15072
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "List": [
            {
                "ActivityId": 1,
                "FormSessionList": [
                    "abc"
                ],
                "Name": "abc",
                "CompanyName": "abc",
                "Mail": "abc",
                "Position": "abc",
                "CountryCode": "abc",
                "Phone": "abc",
                "Agreement": 1,
                "ParticipationMode": 1,
                "ContactInfo": {
                    "AgreeMail": 1,
                    "AgreeSms": 1,
                    "AgreePhone": 1
                },
                "CreatedAt": "abc",
                "UpdatedAt": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

