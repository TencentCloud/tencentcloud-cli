**Example 1: 示例**



Input: 

```
tccli tandon GetUserTicketList --cli-unfold-argument  \
    --ServiceChannel 37 \
    --PostUin 5435345
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "WaitingCount": 0,
            "HandlingCount": 0,
            "Data": [
                {
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
                    "ThirdLevelName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

