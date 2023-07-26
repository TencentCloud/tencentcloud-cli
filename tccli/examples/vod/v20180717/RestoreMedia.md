**Example 1: 使用极速模式解冻媒体文件**

使用极速模式解冻媒体文件

Input: 

```
tccli vod RestoreMedia --cli-unfold-argument  \
    --FileIds 5285485487985271487 \
    --RestoreDay 1 \
    --RestoreTier Expedited
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

