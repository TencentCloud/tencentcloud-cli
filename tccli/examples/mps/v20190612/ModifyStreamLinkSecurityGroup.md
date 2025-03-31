**Example 1: 请求示例**

更新安全组。

Input: 

```
tccli mps ModifyStreamLinkSecurityGroup --cli-unfold-argument  \
    --Id 019202e96d9f09dc0f325e7f7a2a \
    --Name live_test \
    --Whitelist 0.0.0.0
```

Output: 
```
{
    "Response": {
        "RequestId": "01937702c54509dc0f3269ca341f"
    }
}
```

