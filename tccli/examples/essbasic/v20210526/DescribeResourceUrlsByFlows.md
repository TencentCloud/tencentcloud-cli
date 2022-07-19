**Example 1: 根据签署流程信息批量获取资源下载链接**



Input: 

```
tccli essbasic DescribeResourceUrlsByFlows --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.CustomUserId xx \
    --Operator.ProxyIp xx \
    --Operator.Channel xx \
    --FlowIds xx \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.AppId xx
```

Output: 
```
{
    "Response": {
        "FlowResourceUrlInfos": [
            {
                "FlowId": "xx",
                "ResourceUrlInfos": [
                    {
                        "Url": "xx",
                        "Type": "xx",
                        "Name": "xx"
                    }
                ]
            }
        ],
        "ErrorMessages": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

