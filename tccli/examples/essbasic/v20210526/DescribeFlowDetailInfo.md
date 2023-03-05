**Example 1: 查询签署流程合同的详细信息**

查询签署流程合同的详细信息

Input: 

```
tccli essbasic DescribeFlowDetailInfo --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 子客企业经办人id \
    --Agent.ProxyOrganizationOpenId 子客企业第三方id \
    --Agent.AppId 16fd2f7d7xxxxx5f8d501d57b5ec \
    --FlowIds yDxjGUUgydjxxxxxzjERvGKmZJeX
```

Output: 
```
{
    "Response": {
        "ApplicationId": "16fd2f7d7axxxxxd501d57b5ec",
        "FlowInfo": [
            {
                "CreateOn": 1638954201,
                "CustomData": "{\"hello\": 123}",
                "DeadLine": 1689688460,
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "",
                        "ApproveName": "签署方1",
                        "ApproveStatus": "PENDING",
                        "ApproveTime": 0,
                        "ApproveType": "PERSON",
                        "Mobile": "签署方手机号码(11位数字)",
                        "ProxyOperatorOpenId": "us-a9f05aaxxxxxe963ff3f935d7fa39",
                        "ProxyOrganizationName": "第三方平台子客企业名称",
                        "ProxyOrganizationOpenId": "第三方平台子客企业OpenId",
                        "ReceiptId": "签署人信息",
                        "SignOrder": 1
                    },
                    {
                        "ApproveMessage": "",
                        "ApproveName": "签署方2",
                        "ApproveStatus": "PENDING",
                        "ApproveTime": 0,
                        "ApproveType": "ORGANIZATION",
                        "Mobile": "签署方手机号码(11位数字)",
                        "ProxyOperatorOpenId": "us-a9f05axxxxxf935d7fa39",
                        "ProxyOrganizationName": "第三方平台子客企业名称",
                        "ProxyOrganizationOpenId": "第三方平台子客企业OpenId",
                        "ReceiptId": "签署人信息",
                        "SignOrder": 0
                    }
                ],
                "FlowId": "yDxjGUUgxxxxxvGKmZJeX",
                "FlowMessage": "",
                "FlowName": "示例1",
                "FlowStatus": "INIT",
                "FlowType": "示例"
            }
        ],
        "ProxyOrganizationOpenId": "第三方平台子客企业OpenId",
        "FlowGroupName": "",
        "FlowGroupId": "",
        "RequestId": "s16399xxxx603599"
    }
}
```

