**Example 1: ModifyLoginWhiteLearnEDR**

修改异常登录自学习白名单（全部资产 + 剔除主机）

Input: 

```
tccli csip ModifyLoginWhiteLearnEDR --cli-unfold-argument  \
    --Id 39781687 \
    --Places.0.CountryId 1 \
    --Places.0.ProvinceId 1 \
    --Places.0.CityId 1 \
    --RuleAppId 260199983 \
    --Remark 备注2 \
    --Scope 0 \
    --InstanceIDsWithAppId.0.AppId 260199983 \
    --InstanceIDsWithAppId.0.InstanceID ins-2zltluch
```

Output: 
```
{
    "Response": {
        "RequestId": "6f81cb29-2f49-49e3-b27b-f7062ea5841e"
    }
}
```

