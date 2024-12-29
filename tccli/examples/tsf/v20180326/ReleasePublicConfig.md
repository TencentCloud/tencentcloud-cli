**Example 1: 发布公共配置**



Input: 

```
tccli tsf ReleasePublicConfig --cli-unfold-argument  \
    --ConfigId dcfg-p-vkj5dnky \
    --NamespaceId namespace-vw46q85y \
    --ReleaseDesc This is desc
```

Output: 
```
{
    "Response": {
        "RequestId": "d60fcd87-e9d0-475c-89f5-1e76a035d404",
        "Result": true
    }
}
```

