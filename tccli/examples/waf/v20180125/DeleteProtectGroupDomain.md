**Example 1: 解除防护对象组中的域名绑定**



Input: 

```
tccli waf DeleteProtectGroupDomain --cli-unfold-argument  \
    --GroupId 11101 \
    --Domain www.testwaf.com
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

