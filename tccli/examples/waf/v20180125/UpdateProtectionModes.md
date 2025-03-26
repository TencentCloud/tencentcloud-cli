**Example 1: 更新Tiga引擎下大类规则的防护模式**



Input: 

```
tccli waf UpdateProtectionModes --cli-unfold-argument  \
    --Domain www.testwaf.com \
    --Edition clb-waf \
    --TypeIDs 01000111 \
    --Mode 0
```

Output: 
```
{
    "Response": {
        "CommonRsp": {
            "Code": 0,
            "Msg": "success"
        },
        "RequestId": "3bd023947880421b3662db4abe"
    }
}
```

