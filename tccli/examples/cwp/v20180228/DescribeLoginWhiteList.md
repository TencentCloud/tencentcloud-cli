**Example 1: 获取异地登录白名单列表**

获取异地登录白名单列表

Input: 

```
tccli cwp DescribeLoginWhiteList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "LoginWhiteLists": [
            {
                "UserName": "xx",
                "Uuid": "xx",
                "Places": [
                    {
                        "CityId": 1,
                        "CountryId": 1,
                        "ProvinceId": 1
                    },
                    {
                        "CityId": 1,
                        "CountryId": 1,
                        "ProvinceId": 1
                    }
                ],
                "MachineName": "xx",
                "HostIp": "xx",
                "IsGlobal": true,
                "CreateTime": "2020-09-22 00:00:00",
                "StartTime": "xx",
                "ModifyTime": "2020-09-22 00:00:00",
                "SrcIp": "xx",
                "EndTime": "xx",
                "Id": 1
            },
            {
                "UserName": "xx",
                "Uuid": "xx",
                "Places": [
                    {
                        "CityId": 1,
                        "CountryId": 1,
                        "ProvinceId": 1
                    }
                ],
                "MachineName": "xx",
                "ModifyTime": "2020-09-22 00:00:00",
                "IsGlobal": true,
                "Id": 1,
                "StartTime": "xx",
                "HostIp": "xx",
                "SrcIp": "xx",
                "EndTime": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

