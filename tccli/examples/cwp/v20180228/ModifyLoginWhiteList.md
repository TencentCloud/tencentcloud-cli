**Example 1: 编辑异地登录白名单规则**



Input: 

```
tccli cwp ModifyLoginWhiteList --cli-unfold-argument  \
    --Rules.Places.0.CityId 1 \
    --Rules.Places.0.ProvinceId 1 \
    --Rules.Places.0.CountryId 1 \
    --Rules.SrcIp 10.1.1.1 \
    --Rules.UserName admin,root \
    --Rules.IsGlobal true \
    --Rules.HostIp 10.2.2.2 \
    --Rules.EndTime ""
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

