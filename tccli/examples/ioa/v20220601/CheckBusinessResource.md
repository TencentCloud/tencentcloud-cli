**Example 1: 在存相同业务资源**



Input: 

```
tccli ioa CheckBusinessResource --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 0,
                "PageNum": 0,
                "Total": 1,
                "PageCount": 0
            },
            "Items": [
                {
                    "AreaId": 7,
                    "ServiceId": 7,
                    "ServiceType": "domain",
                    "ServiceAddress": "*tencent1658369667.com",
                    "ServiceName": "apitest_service_1658369667",
                    "ServicePort": "all",
                    "CreateTime": "2022-07-21 10:14:30",
                    "UpdateTime": "2022-07-21 10:14:30",
                    "Remark": "",
                    "SmartGateIds": {},
                    "Protocol": 2,
                    "Levels": 5000
                }
            ]
        },
        "RequestId": "1658369670.4525998"
    }
}
```

**Example 2: 不在存相同业务资源**



Input: 

```
tccli ioa CheckBusinessResource --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": {},
            "Page": {
                "PageSize": 0,
                "PageNum": 0,
                "Total": 0,
                "PageCount": 0
            }
        },
        "RequestId": "1658369667.1234992"
    }
}
```

