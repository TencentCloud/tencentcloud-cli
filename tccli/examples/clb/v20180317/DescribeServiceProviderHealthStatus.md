**Example 1: 检查BYOK下模型的健康状态**



Input: 

```
tccli clb DescribeServiceProviderHealthStatus --cli-unfold-argument  \
    --ServiceProviderId byok-ldgl4ojr \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "HealthCheckResults": [
            {
                "Model": "gpt-4o",
                "ProviderKeyId": "mkey-pqqjys9x",
                "Status": "Unknown"
            }
        ],
        "TotalCount": 1,
        "RequestId": "f7dc2bb1-c99f-422b-93bd-9a32db701ea9"
    }
}
```

