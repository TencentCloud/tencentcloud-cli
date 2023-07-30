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
        "ApplicationId": "yDwcC******ciRHST9jtYB",
        "FlowGroupId": "",
        "FlowGroupName": "",
        "FlowInfo": [
            {
                "CcInfos": [],
                "CreateOn": 1686120086,
                "CustomData": "",
                "DeadLine": 1717656086,
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "",
                        "ApproveName": "张三",
                        "ApproveStatus": "PENDING",
                        "ApproveTime": 0,
                        "ApproveType": "PERSON",
                        "Mobile": "133*****75",
                        "ProxyOperatorOpenId": "oHeIG5gF****TXeXZrb4",
                        "ProxyOrganizationName": "",
                        "ProxyOrganizationOpenId": "",
                        "ReceiptId": "yDwg4UUc****QEAn6BWc39jZVY",
                        "SignOrder": 0
                    }
                ],
                "FlowId": "yDwg4UUc******6CLBKPEvnl",
                "FlowMessage": "",
                "FlowName": "电子合同",
                "FlowStatus": "INIT",
                "FlowType": "",
                "NeedCreateReview": false
            }
        ],
        "ProxyOrganizationOpenId": "t1td99d*****d28ec280dd4",
        "RequestId": "c1f80560-****-ae0be7462559"
    }
}
```

