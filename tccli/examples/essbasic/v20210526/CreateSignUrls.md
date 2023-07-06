**Example 1: 批量创建签署参与者签署H5链接**

创建链接,适用于APP或者小程序跳转

Input: 

```
tccli essbasic CreateSignUrls --cli-unfold-argument  \
    --FlowIds test-flow-id \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.AppId test \
    --Endpoint APP
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            "test"
        ],
        "SignUrlInfos": [
            {
                "SignUrl": "test",
                "OrganizationName": "test",
                "Name": "test",
                "ApproverType": "test",
                "Mobile": "test",
                "CustomUserId": "test",
                "Deadline": 0,
                "SignOrder": 0,
                "SignId": "test",
                "IdCardNumber": "testtesttestx",
                "OpenId": "test",
                "FlowId": "test-flow-id",
                "FlowGroupId": ""
            }
        ],
        "RequestId": "test"
    }
}
```

