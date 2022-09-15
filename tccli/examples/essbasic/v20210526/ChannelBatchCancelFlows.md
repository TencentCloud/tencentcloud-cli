**Example 1: 电子签渠道版-根据签署流程id批量撤销合同**

指定需要批量撤销的签署流程Id，批量撤销合同
客户指定需要撤销的签署流程Id，最多100个，超过100不处理；接口失败后返回错误信息

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
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
        "FailMessages": [
            "",
            ""
        ],
        "RequestId": "xx"
    }
}
```

