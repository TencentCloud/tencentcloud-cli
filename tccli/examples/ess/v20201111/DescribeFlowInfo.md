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
                "FlowName": "xx",
                "FlowStatus": 0,
                "FlowDescription": "xx",
                "CreatedOn": 0,
                "FlowMessage": "xx",
                "FlowId": "xx",
                "FlowType": "xx",
                "FlowApproverInfos": [
                    {
                        "CustomApproverTag": "xx",
                        "OrganizationName": "xx",
                        "ApproveName": "xx",
                        "ApproveMessage": "xx",
                        "Mobile": "xx",
                        "ReceiptId": "xx",
                        "CustomUserId": "xx",
                        "ApproveStatus": 0,
                        "OrganizationId": "xx",
                        "ApproverSource": "xx",
                        "ApproveTime": 0,
                        "ApproveType": "xx",
                        "SignOrder": 0
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

