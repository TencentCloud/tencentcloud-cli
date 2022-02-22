**Example 1: 查询个人帐号**



Input: 

```
tccli essbasic DescribeFlowApprovers --cli-unfold-argument  \
    --Caller.ApplicationId  \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --FlowId  \
    --UserId  \
    --SignId 
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "FlowId": "",
        "Approvers": [
            {
                "UserId": "",
                "VerifyChannel": [
                    "WEIXINAPP",
                    "FACEID"
                ],
                "ApproveStatus": 0,
                "ApproveMessage": "",
                "ApproveTime": 0,
                "SubOrganizationId": "",
                "JumpUrl": "",
                "ComponentSeals": [
                    {
                        "ComponentId": "",
                        "SealId": ""
                    }
                ],
                "IsFullText": true,
                "PreReadTime": 30,
                "Mobile": "",
                "Deadline": 0,
                "Name": "",
                "IdCardType": "ID_CARD",
                "IdCardNumber": "",
                "CallbackUrl": "",
                "CanOffLine": false,
                "IsLastApprover": false,
                "SignId": "",
                "SmsTemplate": {
                    "TemplateId": "",
                    "Sign": ""
                }
            }
        ]
    }
}
```

