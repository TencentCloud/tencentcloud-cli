**Example 1: 添加异地登录白名单**



Input: 

```
tccli yunjing AddLoginWhiteList --cli-unfold-argument  \
    --Rules.0.CityId 1 \
    --Rules.0.ProvinceId 1 \
    --Rules.0.CountryId 1 \
    --Rules.SrcIp 10.1.1.1 \
    --Rules.UserName admin \
    --Rules.IsGlobal false \
    --Rules.HostIp 10.2.2.2
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

