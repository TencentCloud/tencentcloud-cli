**Example 1: DescribeLoginWhiteLearnListEDR**

查询异常登录自学习白名单列表

Input: 

```
tccli csip DescribeLoginWhiteLearnListEDR --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AutoLearnEnable": true,
        "List": [
            {
                "Type": "Learn",
                "AppId": 1250000000,
                "Id": 42383278,
                "SrcIp": "",
                "UserName": "",
                "StartTime": "",
                "EndTime": "",
                "Places": [
                    {
                        "CountryId": 1,
                        "ProvinceId": 19,
                        "CityId": 197,
                        "Location": "中国-广东-深圳"
                    },
                    {
                        "CountryId": 1,
                        "ProvinceId": 99999,
                        "CityId": 99999,
                        "Location": "中国-全部省份"
                    }
                ],
                "Locations": "中国-广东-深圳,中国-全部省份",
                "Scope": 0,
                "QUUIDS": [
                    "cd7eba4e-3a35-4e3d-aa41-8fce6c46e8ff"
                ],
                "InstanceIDs": [
                    "ins-xxxxxxxx"
                ],
                "ExcludeQUUIDS": [],
                "ExcludeInstanceIDs": [],
                "TagItems": [],
                "HostCount": 1,
                "Remark": "",
                "CreateTime": "2026-10-20 09:00:00",
                "ModifyTime": "2026-10-21 09:00:00"
            }
        ],
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

