**Example 1: CMR实例解绑指定BYOK实例以及ModelGroup**

CMR实例解绑指定BYOK实例以及ModelGroup

Input: 

```
tccli clb DisassociateModelsFromModelRouter --cli-unfold-argument  \
    --ModelRouterId cmr-5wsfq9lw \
    --Models.0.ModelName my-gpt-5 \
    --Models.0.Provider openai \
    --Models.0.Type BYOK \
    --Models.0.ServiceProviderId byok-74gzz96q
```

Output: 
```
{
    "Response": {
        "RequestId": "e9604e31-5648-4037-83b3-1abfb654bf98"
    }
}
```

