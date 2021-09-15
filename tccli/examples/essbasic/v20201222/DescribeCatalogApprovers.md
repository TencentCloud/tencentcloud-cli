**Example 1: 拉取目录参与者的列表**



Input: 

```
tccli essbasic DescribeCatalogApprovers --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --CatalogId 目录ID \
    --UserId 
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Approvers": [
            {
                "FlowId": "流程ID",
                "Approvers": [
                    {
                        "UserId": "参与者用户ID",
                        "VerifyChannel": [
                            "认证方式"
                        ],
                        "ApproveStatus": 0,
                        "ApproveMessage": "",
                        "ApproveTime": 0,
                        "SubOrganizationId": "参与者所属于机构ID",
                        "JumpUrl": "回调URL",
                        "ComponentSeals": [
                            {
                                "ComponentId": "签署区ID",
                                "SealId": "印章ID"
                            }
                        ],
                        "Mobile": "签署人手机号(脱敏)",
                        "Name": "签署人姓名",
                        "IdCardNumber": "签署人身份证号(脱敏)",
                        "Deadline": 1610682417,
                        "IsLastApprover": true,
                        "SmsTemplate": {
                            "TemplateId": "短信模板ID",
                            "Sign": "短信签名内容"
                        },
                        "IsFullText": true,
                        "PreReadTime": 14
                    }
                ]
            }
        ]
    }
}
```

