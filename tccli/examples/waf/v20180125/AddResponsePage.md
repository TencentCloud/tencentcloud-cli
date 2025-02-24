**Example 1: 添加自定义响应页面**

添加自定义响应页面

Input: 

```
tccli waf AddResponsePage --cli-unfold-argument  \
    --Name good \
    --Status 502 \
    --ContentType application/json \
    --Html testaaaaaaaaaaaaaa
```

Output: 
```
{
    "Response": {
        "RequestId": "90e0db5b-bfaf-43d7-9929-ebf55176e293"
    }
}
```

