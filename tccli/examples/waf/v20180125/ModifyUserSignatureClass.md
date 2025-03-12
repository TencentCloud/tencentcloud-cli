**Example 1: 切换Tiga引擎规则类型的生效开关**



Input: 

```
tccli waf ModifyUserSignatureClass --cli-unfold-argument  \
    --Domain www.test.com \
    --TypeID 010000000 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "TypeID": "010000000",
        "Status": 0,
        "RequestId": "f5063595-f20c-4fa8-9ae4-aed9f16dcb43"
    }
}
```

