**Example 1: 更新Tiga引擎下大类规则的防护模式**



Input: 

```
tccli waf UpdateProtectionModes --cli-unfold-argument  \
    --Domain abc \
    --Edition abc \
    --TypeIDs abc \
    --Mode 0
```

Output: 
```
{
    "Response": {
        "CommonRsp": {
            "Code": 0,
            "Msg": "abc"
        },
        "RequestId": "abc"
    }
}
```

