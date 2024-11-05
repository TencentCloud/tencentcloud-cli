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
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c",
        "LoginWhiteLists": [
            {
                "UserName": "root",
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
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
                "MachineName": "机器名称",
                "HostIp": "1.1.1.1",
                "IsGlobal": true,
                "CreateTime": "2020-09-22 00:00:00",
                "StartTime": "2020-09-22 00:00:00",
                "ModifyTime": "2020-09-22 00:00:00",
                "SrcIp": "1.1.1.1",
                "EndTime": "2020-09-22 00:00:00",
                "Id": 1
            }
        ]
    }
}
```

