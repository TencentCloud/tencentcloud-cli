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
                "CcInfos": [],
                "CreatedOn": 1690441826,
                "Creator": "yDwn4UU*******T1O0OE8jpG5BS",
                "FlowApproverInfos": [
                    {
                        "ApproveMessage": "",
                        "ApproveName": "张小二",
                        "ApproveStatus": 8,
                        "ApproveTime": 0,
                        "ApproveType": "PERSON",
                        "ApproverSource": "",
                        "CustomApproverTag": "",
                        "CustomUserId": "",
                        "Mobile": "1*******64",
                        "OrganizationId": "",
                        "OrganizationName": "",
                        "ReceiptId": "yDwFoUUywgo*******QahgwEmeOw",
                        "SignOrder": 0
                    }
                ],
                "FlowDescription": "",
                "FlowId": "yDwhIUUf*******tSuWZWJuzI0Zv",
                "FlowMessage": "",
                "FlowName": "张小二开店合同",
                "FlowStatus": 8,
                "FlowType": ""
            }
        ],
        "FlowGroupId": "",
        "FlowGroupName": "",
        "RequestId": "9b4490d3-5f0f-4873-8076-0b2839ec6e24"
    }
}
```

