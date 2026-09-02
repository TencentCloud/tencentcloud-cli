**Example 1: 输入多模态能力检测**



Input: 

```
tccli clb TestModelInputModalities --cli-unfold-argument  \
    --Model chat \
    --ProviderKey sk-or-v1-************************************************************07c5 \
    --AccessType PrivateCustom \
    --ApiBase https://openrouter.ai/api/v1 \
    --ServiceProviderId byok-l1l4echw
```

Output: 
```
{
    "Response": {
        "Model": "chat",
        "ProbeDetails": [
            {
                "ErrorInfo": {
                    "ErrorStatus": "UpstreamServiceError",
                    "HttpCode": 500,
                    "OriginalMessage": "Unable to determine text input support (probe failed with HTTP 500)."
                },
                "Modality": "text",
                "Status": "Inconclusive"
            }
        ],
        "SupportedModalities": [],
        "RequestId": "e488fac5-b43e-4dc7-8fc8-c5852f3da0ff"
    }
}
```

