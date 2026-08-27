**Example 1: 创建 BYOK Model**



Input: 

```
tccli clb CreateModel --cli-unfold-argument  \
    --AccessType PrivateCustom \
    --ModelProvider openai \
    --ModelIds.0.ModelId gpt-40 \
    --Keys.0.ApiKey skey-xasd123fasdadcasdasasd \
    --Keys.0.Name ekko-test \
    --ServiceProviderName textbyok-publicbyok \
    --Protocol openai \
    --ApiBases.0.Protocol chat \
    --ApiBases.0.ApiBase https://example.com \
    --VerifySSL False \
    --CMRPrivateNetworkTunnelId pnt-lbepdi5o
```

Output: 
```
{
    "Response": {
        "KeyIds": [
            "mkey-oieh9r1e"
        ],
        "ServiceProviderId": "byok-m910btm4",
        "RequestId": "82771acb-a2fe-4c42-8f90-ba4b21ea67fe"
    }
}
```

