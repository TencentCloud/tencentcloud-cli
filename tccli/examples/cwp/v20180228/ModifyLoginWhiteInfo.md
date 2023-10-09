**Example 1: 编辑登录审计白名单**

编辑登录审计白名单

Input: 

```
tccli cwp ModifyLoginWhiteInfo --cli-unfold-argument  \
    --HostLoginWhiteObj.Places.0.CityId 111 \
    --HostLoginWhiteObj.Places.0.ProvinceId 11 \
    --HostLoginWhiteObj.Places.0.CountryId 1 \
    --HostLoginWhiteObj.SrcIp 1.2.3.4 \
    --HostLoginWhiteObj.UserName "aaa" \
    --HostLoginWhiteObj.Id 128 \
    --HostLoginWhiteObj.Remark "updateRemark1"
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

