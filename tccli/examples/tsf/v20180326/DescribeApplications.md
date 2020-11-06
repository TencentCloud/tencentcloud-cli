**Example 1: 查询应用列表示例**



Input: 

```
tccli tsf DescribeApplications --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --SearchWord driverapi
```

Output: 
```
{
    "Response": {
        "RequestId": "efa09114-e0c3-43ec-8347-5f4454696c61",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ApplicationId": "application-xxxxxxx",
                    "ApplicationName": "test",
                    "ApplicationDesc": null,
                    "ApplicationType": "V",
                    "MicroserviceType": "N",
                    "ProgLang": "J",
                    "CreateTime": "2019-05-17 14:26:38",
                    "UpdateTime": "2019-05-17 14:26:38"
                }
            ]
        }
    }
}
```

