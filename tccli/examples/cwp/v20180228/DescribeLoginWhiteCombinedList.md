**Example 1: 获取登录审计白名单列表-支持新版本筛选**

获取登录审计白名单列表-支持新版本筛选

Input: 

```
tccli cwp DescribeLoginWhiteCombinedList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "LoginWhiteCombinedInfos": [
            {
                "UserName": "xx",
                "Remark": "xx",
                "Name": "xx",
                "Places": [
                    {
                        "CityId": 1,
                        "CountryId": 1,
                        "ProvinceId": 1
                    }
                ],
                "Locale": "xx",
                "IsGlobal": 1,
                "CreateTime": "xx",
                "Uuid": "xx",
                "StartTime": "xx",
                "ModifyTime": "xx",
                "SrcIp": "xx",
                "EndTime": "xx",
                "Id": 1,
                "Desc": "xx"
            }
        ]
    }
}
```

