**Example 1: 获取异地登录白名单列表**

获取异地登录白名单列表

Input: 

```
tccli yunjing DescribeLoginWhiteList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": "2",
        "LoginWhiteLists": [
            {
                "Id": 1,
                "Uuid": "d2973ed0-6334-11e8-87cc-92be94217eaa",
                "Places": [
                    {
                        "CountryId": "1",
                        "ProvinceId": "1",
                        "CityId": "1"
                    },
                    {
                        "CountryId": "1",
                        "ProvinceId": "2",
                        "CityId": "2"
                    }
                ],
                "CreateTime": "2019-09-09 11:00:02",
                "ModifyTime": "2019-09-09 15:37:31",
                "UserName": "guest, abc, 123",
                "SrcIp": "8.8.8.8, 192.168.0.1/24",
                "Quuid": "910c95a5-04b1-4d99-aa3c-a261e51b81bf",
                "IsGlobal": true
            },
            {
                "Id": 2,
                "Uuid": "fb8c1b1a-5e2c-11e8-bb3b-00e021e1b24b",
                "Places": [
                    {
                        "CountryId": "1",
                        "ProvinceId": "1",
                        "CityId": "1"
                    }
                ],
                "CreateTime": "2019-09-09 11:00:02",
                "ModifyTime": "2019-09-09 11:00:02",
                "UserName": "guest",
                "SrcIp": "10.1.1.1, 192.168.0.1/24",
                "Quuid": "910c95a5-04b1-4d99-aa3c-a261e51b81bf",
                "IsGlobal": true
            }
        ],
        "RequestId": "8bcb699a-5ba3-ebcf-f569-d5f5e5271414"
    }
}
```

