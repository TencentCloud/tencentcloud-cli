**Example 1: 查询个人帐号**



Input: 

```
tccli essbasic DescribeFlow --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.OperatorId a08c79b56afcd3b64317b33bee00ce12 \
    --FlowId 93e2a19ee44a3f93cadeadaae739f1d4
```

Output: 
```
{
    "Response": {
        "CallbackUrl": "",
        "CreatedOn": 1609579241,
        "Creator": {
            "ApplicationId": "c17bdf9c2a7bdcb32611f4d0200fee3d",
            "OperatorId": "a08c79b56afcd3b64317b33bee00ce12",
            "SubOrganizationId": ""
        },
        "Deadline": 1609891200,
        "FlowDescription": "test-20210102",
        "FlowId": "93e2a19ee44a3f93cadeadaae739f1d4",
        "FlowMessage": "",
        "FlowName": "test-20210102-测试发起",
        "FlowStatus": 1,
        "FlowType": "劳务合同",
        "RequestId": "s1609581145205347374",
        "UpdatedOn": 0
    }
}
```

