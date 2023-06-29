**Example 1: 设置应用自定义内容**

设置应用自定义内容

Input: 

```
tccli lcic SetAppCustomContent --cli-unfold-argument  \
    --SdkAppId 123 \
    --CustomContent.0.Scene default \
    --CustomContent.0.LogoUrl https://yourdomain.com/logo.png \
    --CustomContent.0.HomeUrl https://yourdomain.com/login \
    --CustomContent.0.JsUrl https://yourdomain.com/default.js \
    --CustomContent.0.CssUrl https://yourdomain.com/default.css
```

Output: 
```
{
    "Response": {
        "RequestId": "213das"
    }
}
```

