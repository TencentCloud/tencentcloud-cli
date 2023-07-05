**Example 1: 解绑溯源码和批次的关系**

解绑溯源码和批次的关系

Input: 

```
tccli trp ModifyTraceCodeUnlink --cli-unfold-argument  \
    --BatchId xfetmgoiky2nms6nk8 \
    --Codes https://anxin.m.qq.com/qr/3a9avhhvk4oyqb
```

Output: 
```
{
    "Response": {
        "UnlinkCnt": 1,
        "CodeCnt": 1,
        "BatchId": "abc",
        "RequestId": "abc"
    }
}
```

