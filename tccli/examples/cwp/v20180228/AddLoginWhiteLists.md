**Example 1: 批量添加异地登录白名单**

入侵检测-登录审计-批量添加异地登录白名单

Input: 

```
tccli cwp AddLoginWhiteLists --cli-unfold-argument  \
    --EventId 11234 \
    --ProcessType Id \
    --HostLoginWhiteObj.UserName xx \
    --HostLoginWhiteObj.Remark xx \
    --HostLoginWhiteObj.Places.0.CityId 0 \
    --HostLoginWhiteObj.Places.0.CountryId 0 \
    --HostLoginWhiteObj.Places.0.ProvinceId 135 \
    --HostLoginWhiteObj.IsGlobal 0 \
    --HostLoginWhiteObj.HostInfos.0.Quuid 66640e61-aaaa-4632-aaaa-aaaa037e7ba0 \
    --HostLoginWhiteObj.HostInfos.0.Uuid 66640e61-aaaa-4632-aaaa-aaaa037e7ba0 \
    --HostLoginWhiteObj.StartTime 00:00 \
    --HostLoginWhiteObj.SrcIp 1.2.3.4 \
    --HostLoginWhiteObj.EndTime 00:01
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "Error": {
            "Code": "InvalidParameter.RuleHostipErr",
            "Message": "无对应主机信息"
        }
    }
}
```

