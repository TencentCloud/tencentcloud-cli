**Example 1: 检查管理员和成员企业实名是否互信**



Input: 

```
tccli organization CheckMemberAuthRelation --cli-unfold-argument  \
    --HostUin 100000547473 \
    --MemberUins 100000547476 100000547476
```

Output: 
```
{
    "Response": {
        "CheckStatus": [
            {
                "Message": "auth info not same",
                "Code": "FailedOperation.AuthInfoNotSame",
                "MemberUin": 100000547476
            },
            {
                "Message": "Success",
                "Code": "Success",
                "MemberUin": 100000547475
            }
        ],
        "RequestId": "e1fac9c7-5663-401d-90bd-522b60f8b689"
    }
}
```

