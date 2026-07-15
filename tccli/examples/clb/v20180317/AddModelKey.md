**Example 1: 自定义模型添加Key**



Input: 

```
tccli clb AddModelKey --cli-unfold-argument  \
    --ServiceProviderId byok-c8xrjgpt \
    --Keys.0.ApiKey 2d \
    --Keys.0.Name d
```

Output: 
```
{
    "Response": {
        "KeyIds": [
            "mkey-0a8htk6l"
        ],
        "RequestId": "02f6124d-892c-4947-99e2-7237f60ad3e8"
    }
}
```

