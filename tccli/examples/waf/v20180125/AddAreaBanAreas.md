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
        "RequestId": "8d630afc-0da8-43f6-862a-045e21ebfdba"
    }
}
```

