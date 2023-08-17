**Example 1: 异步操作完成业务回调通知计费**

异步操作完成业务回调通知计费

Input: 

```
tccli billing CallbackAsyncOperateResp --cli-unfold-argument  \
    --ProductCode p_xxx \
    --ReferenceId 029e0413c8954e0c830c121d202675b6 \
    --OperateResult 0 \
    --ResourceSet.0.ResourceId ins-1111 \
    --ResourceSet.0.OperateResult 1 \
    --ResourceSet.0.Message  \
    --ResourceSet.0.OperateEndTime 2022-06-23 15:28:17 \
    --ResourceSet.0.ZoneId 200008 \
    --ResourceSet.1.ResourceId ins-2222 \
    --ResourceSet.1.OperateResult 1 \
    --ResourceSet.1.Message  \
    --ResourceSet.1.OperateEndTime 2022-06-23 15:28:18 \
    --ResourceSet.1.ZoneId 200008
```

Output: 
```
{
    "Response": {
        "CallbackSuccess": true,
        "RequestId": "061cb05c-28ad-46e8-b744-37c01bdfca32"
    }
}
```

