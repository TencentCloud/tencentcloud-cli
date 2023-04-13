**Example 1: 获取批量撤销签署流程链接**

电子签企业版：指定需要批量撤回的签署流程Id，获取批量撤销链接
客户指定需要撤回的签署流程Id，最多100个，超过100不处理；接口调用成功返回批量撤回合同的链接，通过链接跳转到电子签小程序完成批量撤回

Input: 

```
tccli ess CreateBatchCancelFlowUrl --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowIds 1 2
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
        "RequestId": "test"
    }
}
```

