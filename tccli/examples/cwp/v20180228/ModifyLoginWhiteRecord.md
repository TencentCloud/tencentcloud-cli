**Example 1: 编辑登录审计白名单**

编辑登录审计白名单

Input: 

```
tccli cwp ModifyLoginWhiteRecord --cli-unfold-argument  \
    --UserName xx \
    --Remark xx \
    --Places.0.CityId 1 \
    --Places.0.CountryId 1 \
    --Places.0.ProvinceId 1 \
    --IsGlobal 1 \
    --Hosts.0.Quuid xx \
    --Hosts.0.Uuid xx \
    --StartTime xx \
    --SrcIp xx \
    --EndTime xx \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

