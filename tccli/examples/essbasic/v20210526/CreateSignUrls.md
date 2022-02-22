**Example 1: 批量创建签署参与者签署H5链接**



Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --FlowIds test-flow-id \
    --Agent.ProxyAppId c17bdf9c 2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.AppId xx \
    --Endpoint CHANNEL
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            "xx"
        ],
        "SignUrlInfos": [
            {
                "SignUrl": "xx",
                "OrganizationName": "xx",
                "Name": "xx",
                "ApproverType": "xx",
                "Mobile": "xx",
                "CustomUserId": "xx",
                "Deadline": 0,
                "SignOrder": 0,
                "SignId": "xx",
                "IdCardNumber": "xxxxxxx",
                "OpenId": "xx",
                "FlowId": "test-flow-id"
            }
        ],
        "RequestId": "xx"
    }
}
```

