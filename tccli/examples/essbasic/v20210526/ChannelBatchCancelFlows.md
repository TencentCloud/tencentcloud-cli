**Example 1: 根据签署流程id批量撤销合同**

指定需要批量撤销的签署流程Id，批量撤销合同
客户指定需要撤销的签署流程Id，最多100个，超过100不处理；接口失败后返回错误信息

Input: 

```
tccli essbasic ChannelBatchCancelFlows --cli-unfold-argument  \
    --FlowIds testx \
    --Agent.ProxyOperator.OpenId testx \
    --Agent.AppId testx \
    --Agent.ProxyOrganizationOpenId testx \
    --CancelMessage 撤销测试 \
    --CancelMessageFormat 0
```

Output: 
```
{
    "Response": {
        "FailMessages": [],
        "RequestId": "c5e01d20-xxxxxx09d3d32b00"
    }
}
```

