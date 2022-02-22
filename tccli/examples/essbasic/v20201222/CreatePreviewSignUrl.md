**Example 1: 生成签署链接**



Input: 

```
tccli essbasic CreatePreviewSignUrl --cli-unfold-argument  \
    --FlowId 94b3f7921f0642940138573ca8361220 \
    --Deadline 1637063713 \
    --Caller.OperatorId a08c79b56afcd3b64317b33bee00ce12 \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId fb695ea161c7d7c46c7dbd35f4050ef6
```

Output: 
```
{
    "Response": {
        "RequestId": "s1610023745620372661",
        "PreviewSignUrl": "https://essurl.cn/SDKU0E"
    }
}
```

