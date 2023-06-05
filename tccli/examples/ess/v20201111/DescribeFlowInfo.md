**Example 1: 查询合同详情**

查询合同详情

Input: 

```
tccli ess DescribeFlowInfo --cli-unfold-argument  \
    --FlowIds c7b5ca37ae*******2b4c6644 61a82f0c1******d0d807
```

Output: 
```
{
    "Response": {
        "FlowDetailInfos": [
            {
                "FlowId": "abc",
                "FlowName": "abc",
                "FlowType": "abc",
                "FlowStatus": 0,
                "FlowMessage": "abc",
                "FlowDescription": "abc",
                "CreatedOn": 0,
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "abc",
                        "ApproveName": "abc",
                        "ApproveStatus": 0,
                        "ReceiptId": "abc",
                        "CustomUserId": "abc",
                        "Mobile": "abc",
                        "SignOrder": 0,
                        "ApproveTime": 0,
                        "ApproveType": "abc",
                        "ApproverSource": "abc",
                        "CustomApproverTag": "abc",
                        "OrganizationId": "abc",
                        "OrganizationName": "abc"
                    }
                ],
                "CcInfos": [
                    {
                        "ApproveMessage": "abc",
                        "ApproveName": "abc",
                        "ApproveStatus": 0,
                        "ReceiptId": "abc",
                        "CustomUserId": "abc",
                        "Mobile": "abc",
                        "SignOrder": 0,
                        "ApproveTime": 0,
                        "ApproveType": "abc",
                        "ApproverSource": "abc",
                        "CustomApproverTag": "abc",
                        "OrganizationId": "abc",
                        "OrganizationName": "abc"
                    }
                ],
                "Creator": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

