**Example 1: 电子签渠道版-根据签署流程id批量撤销合同**

指定需要批量撤销的签署流程Id，批量撤销合同
客户指定需要撤销的签署流程Id，最多100个，超过100不处理；接口失败后返回错误信息

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.ProxyOperator.OpenId xx \
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

**Example 2: 测试**



Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --Operator.OpenId xxx \
    --Operator.ClientIp xx \
    --Operator.CustomUserId xx \
    --Operator.ProxyIp xxx \
    --Operator.Channel xxx \
    --FlowIds xxx \
    --Agent.ProxyAppId xxx \
    --Agent.ProxyOperator.OpenId xxx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xxx \
    --Agent.AppId xxx \
    --Agent.ProxyOrganizationOpenId xxx \
    --Agent.ProxyOrganizationId xxx \
    --CancelMessage 撤销测试 \
    --CancelMessageFormat 0
```

Output: 
```
{
    "Response": {
        "FailMessages": [],
        "RequestId": "c5e01d20-8d10-49f9-9512-d209d3d32b00"
    }
}
```

