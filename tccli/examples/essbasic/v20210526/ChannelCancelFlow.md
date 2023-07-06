**Example 1: 撤销签署流程**

撤销签署流程

Input: 

```
tccli essbasic ChannelCancelFlow --cli-unfold-argument  \
    --Operator.OpenId test \
    --FlowId test \
    --CancelMessage test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test
```

Output: 
```
{
    "Response": {
        "RequestId": "s16221xxxx12775546"
    }
}
```

