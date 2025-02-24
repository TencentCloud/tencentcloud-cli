**Example 1: 域名应用自定义响应页面**

域名应用自定义响应页面

Input: 

```
tccli waf ApplyResponsePage --cli-unfold-argument  \
    --Domain www.qcloudwaf.com \
    --Id 200 \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "90e0db5b-bfaf-43d7-9929-ebf55176e293"
    }
}
```

