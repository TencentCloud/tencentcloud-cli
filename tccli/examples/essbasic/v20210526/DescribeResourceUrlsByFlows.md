**Example 1: 根据签署流程信息批量获取资源下载链接**

根据签署流程信息批量获取资源下载链接

Input: 

```
tccli essbasic DescribeResourceUrlsByFlows --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test \
    --FlowIds test
```

Output: 
```
{
    "Response": {
        "FlowResourceUrlInfos": [
            {
                "FlowId": "123",
                "ResourceUrlInfos": [
                    {
                        "Url": "https://",
                        "Type": "test",
                        "Name": "test"
                    }
                ]
            }
        ],
        "ErrorMessages": [
            ""
        ],
        "RequestId": "12345"
    }
}
```

