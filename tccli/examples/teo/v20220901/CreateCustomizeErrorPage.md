**Example 1: 创建自定义错误页面接口**

创建自定义错误页面接口

Input: 

```
tccli teo CreateCustomizeErrorPage --cli-unfold-argument  \
    --ZoneId zone-2kplomhisdcb \
    --Name web防护自定义错误页面 \
    --Description web防护自定义错误页面 \
    --ContentType application/json \
    --Content {"title":"自定义错误页", "Content":"自定义错误页面内容"}
```

Output: 
```
{
    "Response": {
        "PageId": "p-2kplomhisdcb",
        "RequestId": "9bd9c732-8f9a-4cd3-a3e8-1c9db5e53631"
    }
}
```

