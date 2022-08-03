**Example 1: 电子签渠道版-根据签署流程id创建批量撤回url**

指定需要批量撤回的签署流程Id，获取批量撤销链接
客户指定需要撤回的签署流程Id，最多100个，超过100不处理；接口调用成功返回批量撤回合同的链接，通过链接跳转到电子签小程序完成批量撤回

Input: 

```
tccli essbasic ChannelCreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.AppId xx \
    --FlowIds 
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "url",
        "FailMessages": [
            "",
            ""
        ],
        "UrlExpireOn": "",
        "RequestId": "xx"
    }
}
```

