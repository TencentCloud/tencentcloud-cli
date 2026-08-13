**Example 1: 创建第三方BYOK**



Input: 

```
tccli clb CreateModel --cli-unfold-argument  \
    --AccessType PublicCustom \
    --ModelProvider OpenAI \
    --ModelIds.0.ModelId gpt-4o \
    --Keys.0.ApiKey sk-awdawe12esfd1211d \
    --ApiBase https://deepseek.api.com \
    --HealthCheckConfig.HealthCheckEnabled False
```

Output: 
```
{
    "Response": {
        "KeyIds": [
            "mkey-0b39bh7u"
        ],
        "ServiceProviderId": "byok-dhd4w2eg",
        "RequestId": "1f5b0825-105c-4a52-8b62-65fce5296d92"
    }
}
```

