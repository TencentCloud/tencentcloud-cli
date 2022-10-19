**Example 1: 根据签署流程信息批量获取资源下载链接**



Input: 

```
tccli essbasic DescribeResourceUrlsByFlows --cli-unfold-argument  \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.AppId xx \
    --FlowIds xx
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

