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
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c",
        "LoginWhiteCombinedInfos": [
            {
                "Id": 357790160,
                "Places": [
                    {
                        "CityId": 0,
                        "ProvinceId": 0,
                        "CountryId": 52,
                        "Location": "阿尔及利亚"
                    }
                ],
                "UserName": "root",
                "SrcIp": "1.1.1.1",
                "IsGlobal": 0,
                "CreateTime": "2019-12-25 11:57:15",
                "ModifyTime": "2019-12-25 11:57:15",
                "Locale": "52:0:0,103:0:0,141:0:0,165:0:0,210:0:0,177:0:0",
                "Locations": "阿尔及利亚,阿尔巴尼亚,奥地利,海地,奥兰群岛,安提瓜和巴布达",
                "Remark": "myremark***",
                "StartTime": "2020-11-21 15:16:00",
                "EndTime": "2020-11-21 15:16:00",
                "Name": "cwp",
                "Desc": "1.1.1.1",
                "Uuid": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
            }
        ]
    }
}
```

