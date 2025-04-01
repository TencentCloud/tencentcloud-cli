**Example 1: 请求示例**

创建安全组。

Input: 

```
tccli mps CreateStreamLinkSecurityGroup --cli-unfold-argument  \
    --Name live_test \
    --Whitelist 102.102.102.102/32
```

Output: 
```
{
    "Response": {
        "Id": "019202e96d9f09dc0f325e7f7a2a",
        "RequestId": "01937702c54509dc0f3269ca341f"
    }
}
```

