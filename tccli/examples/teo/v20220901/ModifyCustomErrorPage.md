**Example 1: 修改自定义错误页面**

修改自定义错误页面。

Input: 

```
tccli teo ModifyCustomErrorPage --cli-unfold-argument  \
    --PageId p-2kplomhisdcb \
    --ZoneId zone-2kplomhisdcb \
    --Name web防护自定义错误页面 \
    --Description web防护自定义错误页面 \
    --ContentType application/json \
    --Content {"title": "自定义错误页面title","content": "自定义错误页面内容"}
```

Output: 
```
{
    "Response": {
        "RequestId": "9bd9c732-8f9a-4cd3-a3e8-1c9db5e53631"
    }
}
```

