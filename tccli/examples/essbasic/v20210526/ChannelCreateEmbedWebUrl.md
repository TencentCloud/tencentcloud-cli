**Example 1: 获取创建印章的嵌入WEB链接**

获取创建印章的嵌入WEB链接

Input: 

```
tccli essbasic ChannelCreateEmbedWebUrl --cli-unfold-argument  \
    --BusinessId  \
    --EmbedType CREATE_SEAL \
    --Agent.AppId yDxjb***********8n \
    --Agent.ProxyOrganizationOpenId testOpenId \
    --Agent.ProxyOperator.OpenId testOpenId
```

Output: 
```
{
    "Response": {
        "WebUrl": "https://test.ess.com/seal-create?embed=1&code=testcode&channel=PROXYCHANNEL",
        "RequestId": "2"
    }
}
```

