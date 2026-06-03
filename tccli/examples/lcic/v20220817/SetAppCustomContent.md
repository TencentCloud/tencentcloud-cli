**Example 1: 设置应用自定义内容**

设置应用自定义内容

Input: 

```
tccli lcic SetAppCustomContent --cli-unfold-argument  \
    --SdkAppId 123 \
    --CustomContent.0.Scene default \
    --CustomContent.0.LogoUrl https://example.com/logo.png \
    --CustomContent.0.HomeUrl https://example.com/login \
    --CustomContent.0.JsUrl https://example.com/default.js \
    --CustomContent.0.CssUrl https://example.com/default.css
```

Output: 
```
{
    "Response": {
        "RequestId": "213das"
    }
}
```

