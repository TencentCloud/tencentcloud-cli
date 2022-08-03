**Example 1: 添加保护网站（用户需在第一次提交保护网站时携带企业信息）**



Input: 

```
tccli bma CreateBPProtectURLs --cli-unfold-argument  \
    --CompanyName xxx \
    --Phone xxx \
    --LicenseName xxx \
    --ProtectURLs qq.com baidu.com \
    --ProtectWebs 腾讯网 百度网
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

