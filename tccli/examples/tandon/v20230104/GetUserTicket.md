**Example 1: 示例**



Input: 

```
tccli tandon GetUserTicket --cli-unfold-argument  \
    --TicketId 3927018 \
    --ServiceChannel 37 \
    --PostUin 47326
```

Output: 
```
{
    "Response": {
        "Data": {
            "TicketId": 0,
            "Uin": "abc",
            "OwnerUin": "abc",
            "Question": "abc",
            "ServiceChannel": 0,
            "RelatedPhoneNumber": "abc",
            "RelatedRegionCode": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "ExternStatus": 0,
            "ExternStatusDisplay": "abc",
            "ServiceRate": 0,
            "UnsatisfyReason": 0,
            "HasComplaint": 0,
            "Priority": 0,
            "Appraise": "abc",
            "AppraiseTime": "abc",
            "FirstLevelName": "abc",
            "SecondLevelName": "abc",
            "ThirdLevelName": "abc",
            "ExternOperations": [
                {
                    "OperationId": 0,
                    "ExternReply": "abc",
                    "OperateTime": "abc",
                    "OperatorType": 0,
                    "SecretContent": "abc",
                    "Operator": "abc",
                    "TargetExternStatus": 0,
                    "TargetExternStatusDisplay": "abc"
                }
            ],
            "CustomFieldList": [
                {
                    "FieldId": 1,
                    "FieldName": "abc",
                    "FieldValue": "abc",
                    "Types": "abc",
                    "FieldKV": "abc",
                    "Weights": 1
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

