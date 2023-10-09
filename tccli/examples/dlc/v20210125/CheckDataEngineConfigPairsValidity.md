**Example 1: 检查引擎用户自定义参数的有效性**

本接口用于检查引擎用户自定义参数的有效性。

Input: 

```
tccli dlc CheckDataEngineConfigPairsValidity --cli-unfold-argument  \
    --ChildImageVersionId b8sddsad7-ekd4-4e5e-993e-e5db64fa21c1 \
    --ImageVersionId 
```

Output: 
```
{
    "Response": {
        "IsAvailable": true,
        "UnavailableConfig": [
            "key"
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

