**Example 1: 编辑登录审计白名单**

编辑登录审计白名单

Input: 

```
tccli cwp ModifyLoginWhiteRecord --cli-unfold-argument  \
    --UserName abc \
    --SrcIp abc \
    --StartTime abc \
    --EndTime abc \
    --Remark abc \
    --IsGlobal 1 \
    --Id 1 \
    --Hosts.0.Quuid abc \
    --Hosts.0.Uuid abc \
    --Places.0.CityId 1 \
    --Places.0.ProvinceId 1 \
    --Places.0.CountryId 1 \
    --Places.0.Location abc
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

