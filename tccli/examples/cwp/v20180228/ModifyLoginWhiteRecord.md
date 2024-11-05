**Example 1: 编辑登录审计白名单**

编辑登录审计白名单

Input: 

```
tccli cwp ModifyLoginWhiteRecord --cli-unfold-argument  \
    --UserName root \
    --SrcIp 1.1.1.1.1 \
    --StartTime 2019-12-25 11:57:15 \
    --EndTime 2019-12-25 11:57:15 \
    --Remark 备注 \
    --IsGlobal 1 \
    --Id 1 \
    --Hosts.0.Quuid 05f0bcab-726c-4ea4-8109-bcd03d5598f7 \
    --Hosts.0.Uuid 05f0bcab-726c-4ea4-8109-bcd03d5598f7 \
    --Places.0.CityId 1 \
    --Places.0.ProvinceId 1 \
    --Places.0.CountryId 1 \
    --Places.0.Location 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

