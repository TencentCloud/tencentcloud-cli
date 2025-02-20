**Example 1: 上报用量**



Input: 

```
tccli hunyuan ReportUsage --cli-unfold-argument  \
    --Model hunyuan \
    --SessionId 03e795d9-be77-4d21-b229-54086aa4f456 \
    --Usage.PromptTokens 8 \
    --Usage.CompletionTokens 20 \
    --Usage.TotalTokens 28
```

Output: 
```
{
    "Response": {
        "RequestId": "03e795d9-be77-4d21-b229-54086aa4f456"
    }
}
```

