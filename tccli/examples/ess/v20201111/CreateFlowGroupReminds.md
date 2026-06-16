**Example 1: 合同组催办**



Input: 

```
tccli ess CreateFlowGroupReminds --cli-unfold-argument  \
    --Operator.UserId yDCH5UUckpax3h9wUxHw4XzSpBev1wRg \
    --FlowGroupId yD3**************************jJK
```

Output: 
```
{
    "Response": {
        "RemindFlowGroupRecords": [
            {
                "ApproverName": "叶**",
                "FlowIds": [
                    "yD3**************************VCw"
                ],
                "FlowNames": [
                    "合同组(2份合同)-单C-2"
                ],
                "Mobile": "156****8190",
                "RemindMessageList": [
                    {
                        "ApproverOrder": 0,
                        "Reason": "催办成功（短信）",
                        "SignId": "yD3**************************9gk",
                        "Status": 0
                    }
                ]
            }
        ],
        "RequestId": "52332bdd-67a4-4fb9-9efe-3a051b7c6c5d"
    }
}
```

