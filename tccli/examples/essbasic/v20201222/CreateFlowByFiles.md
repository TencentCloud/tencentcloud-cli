**Example 1: 使用上传文件创建流程**



Input: 

```
tccli essbasic CreateFlowByFiles --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.OperatorId a08c79b56afcd3b64317b33bee00ce12 \
    --FileIds d54e3caec25ad0ea6be24406762b7562 88f967a9e51473ce096478564b369831 \
    --FlowInfo.Deadline 1609891200 \
    --FlowInfo.FlowDescription test-20210102 \
    --FlowInfo.FlowName test-20210102-测试发起-2 \
    --FlowInfo.FlowType 劳务合同 \
    --FlowInfo.UserData 随便写点什么
```

Output: 
```
{
    "Response": {
        "FlowId": "83c210b73a2cd9e40fb9849283e78788",
        "RequestId": "s1609646162664722594"
    }
}
```

