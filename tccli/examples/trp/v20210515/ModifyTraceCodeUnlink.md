**Example 1: 解绑溯源码和批次的关系**

解绑溯源码和批次的关系

Input: 

```
tccli trp ModifyTraceCodeUnlink --cli-unfold-argument  \
    --BatchId 20241022112952826 \
    --Codes https://anxin.m.qq.com/qr/3a9avhhvk4oyqb
```

Output: 
```
{
    "Response": {
        "UnlinkCnt": 1,
        "CodeCnt": 1,
        "BatchId": "20241022112952826",
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

