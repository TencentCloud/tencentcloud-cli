**Example 1: 添加封禁地域**



Input: 

```
tccli waf AddAreaBanAreas --cli-unfold-argument  \
    --Domain test.qcloud.com \
    --Edition clb-waf \
    --Areas 新疆 江西
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

