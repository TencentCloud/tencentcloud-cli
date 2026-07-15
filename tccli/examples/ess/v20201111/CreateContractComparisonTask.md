**Example 1: 创建合同对比任务**

此接口（CreateContractComparisonTask）用于创建合同对比任务。
适用场景：对比两份合同中字段（如：金额、日期、甲方名称等）的内容差异。

Input: 

```
tccli ess CreateContractComparisonTask --cli-unfold-argument  \
    --Operator.UserId yD*****************ZC \
    --DiffFileResourceId yD***************yQ \
    --OriginFileResourceId yD**************Xy \
    --Comment 这是一个合同对比任务 \
    --UserData QmFzZTY0IEJhc2U2NCA \
    --Tags.0.TagKey 电子签 \
    --Tags.0.TagValue 对比任务
```

Output: 
```
{
    "Response": {
        "RequestId": "s1760425670608827095",
        "TaskId": "yD*************Ks",
        "UserData": "QmFzZTY0IEJhc2U2NCA"
    }
}
```

