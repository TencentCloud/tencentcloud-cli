**Example 1: 查询签署流程合同的详细信息**



Input: 

```
tccli essbasic DescribeFlowDetailInfo --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 渠道经办人id \
    --Agent.ProxyOrganizationOpenId 渠道企业第三方id \
    --Agent.AppId 16fd2f7d7ae85d13ca5f8d501d57b5ec \
    --FlowIds yDxjGUUgydjfjp2rUuO4zjERvGKmZJeX
```

Output: 
```
{
    "Response": {
        "ApplicationId": "16fd2f7d7ae85d13ca5f8d501d57b5ec",
        "FlowInfo": [
            {
                "CreateOn": 1638954201,
                "DeadLine": 1689688460,
                "FlowId": "yDxjGUUgydjfjp2rUuO4zjERvGKmZJeX",
                "FlowMessage": "",
                "FlowName": "示例1",
                "FlowStatus": "INIT",
                "FlowType": "示例"
            }
        ],
        "ProxyOrganizationOpenId": "渠道测第三方id",
        "RequestId": "s1639904010686603599"
    }
}
```

