**Example 1: 根据签署流程id创建批量撤回url**

指定需要批量撤回的签署流程Id，获取批量撤销链接
客户指定需要撤回的签署流程Id，最多100个，超过100不处理；接口调用成功返回批量撤回合同的链接，通过链接跳转到电子签小程序完成批量撤回

Input: 

```
tccli essbasic ChannelCreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.AppId test \
    --FlowIds id
```

Output: 
```
{
    "Response": {
        "BatchCancelFlowUrl": "url",
        "FailMessages": [],
        "UrlExpireOn": "",
        "RequestId": "id"
    }
}
```

