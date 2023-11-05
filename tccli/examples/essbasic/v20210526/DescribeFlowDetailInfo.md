**Example 1: 查询本企业创建的两个合同的详细信息**

查询本企业创建的两个合同的详细信息, FlowIds传了两个合同的ID数组

Input: 

```
tccli essbasic DescribeFlowDetailInfo --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowIds yDSLNUUckpos0iylUyzyvt7TwYVXYRh7 yDSLKUUckpoq19jtUxflhN4ugLFOCBNT
```

Output: 
```
{
    "Response": {
        "ApplicationId": "yDwhxUUckp3gl8j5UuFX33LSNozpRsbi",
        "ProxyOrganizationOpenId": "org_dianziqian",
        "FlowInfo": [
            {
                "FlowId": "yDSLKUUckpoq19jtUxflhN4ugLFOCBNT",
                "FlowName": "购买50吨西红柿合同",
                "FlowType": "采购合同",
                "FlowStatus": "INIT",
                "FlowMessage": "",
                "CreateOn": 1698895092,
                "DeadLine": 1730431092,
                "CustomData": "",
                "FlowApproverInfos": [
                    {
                        "ReceiptId": "yDSLOUUckpoj6ocqUyzilW6RdWiojxfG",
                        "ProxyOrganizationOpenId": "org_dianziqian",
                        "ProxyOperatorOpenId": "n9527",
                        "ProxyOrganizationName": "典子谦示例企业",
                        "Mobile": "1850000000",
                        "SignOrder": 0,
                        "ApproveName": "典子谦",
                        "ApproveStatus": "PENDING",
                        "ApproveMessage": "",
                        "ApproveTime": 0,
                        "ApproveType": "ORGANIZATION",
                        "ApproverRoleName": "买方"
                    },
                    {
                        "ReceiptId": "yDSLOUUckpoj6ocjUyzilW6E0SsA8ggh",
                        "ProxyOrganizationOpenId": "",
                        "ProxyOperatorOpenId": "org_zhangsan",
                        "ProxyOrganizationName": "张三谦示例企业",
                        "Mobile": "1730000000",
                        "SignOrder": 0,
                        "ApproveName": "张三",
                        "ApproveStatus": "PENDING",
                        "ApproveMessage": "",
                        "ApproveTime": 0,
                        "ApproveType": "ORGANIZATION",
                        "ApproverRoleName": "卖方"
                    }
                ],
                "CcInfos": [],
                "NeedCreateReview": false
            },
            {
                "FlowId": "yDSLNUUckpos0iylUyzyvt7TwYVXYRh7",
                "FlowName": "购买50吨西瓜合同",
                "FlowType": "采购合同",
                "FlowStatus": "INIT",
                "FlowMessage": "",
                "CreateOn": 1698978129,
                "DeadLine": 1730514129,
                "CustomData": "",
                "FlowApproverInfos": [
                    {
                        "ReceiptId": "yDSLKUUckpoqohr5UcuKmnx5zDmZ7Tl4",
                        "ProxyOrganizationOpenId": "org_dianziqian",
                        "ProxyOperatorOpenId": "n9527",
                        "ProxyOrganizationName": "典子谦示例企业",
                        "Mobile": "1850000000",
                        "SignOrder": 0,
                        "ApproveName": "典子谦",
                        "ApproveStatus": "PENDING",
                        "ApproveMessage": "",
                        "ApproveTime": 0,
                        "ApproveType": "ORGANIZATION",
                        "ApproverRoleName": "买方"
                    },
                    {
                        "ReceiptId": "yDSLKUUckpoqohr0UcuKmnBmx1YdqgMW",
                        "ProxyOrganizationOpenId": "",
                        "ProxyOperatorOpenId": "org_zhangsan",
                        "ProxyOrganizationName": "张三示例企业",
                        "Mobile": "1730000000",
                        "SignOrder": 0,
                        "ApproveName": "张三",
                        "ApproveStatus": "PENDING",
                        "ApproveMessage": "",
                        "ApproveTime": 0,
                        "ApproveType": "ORGANIZATION",
                        "ApproverRoleName": "卖方"
                    }
                ],
                "CcInfos": [],
                "NeedCreateReview": false
            }
        ],
        "FlowGroupId": "",
        "FlowGroupName": "",
        "RequestId": "940b70b6-ef38-4932-ba80-936efe55b601"
    }
}
```

