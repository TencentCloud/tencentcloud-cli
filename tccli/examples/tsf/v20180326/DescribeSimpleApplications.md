**Example 1: 查询简单应用列表**



Input: 

```
tccli tsf DescribeSimpleApplications --cli-unfold-argument  \
    --Offset 50 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "3f39fc04-9a07-4b70-bb56-47ff8eb051df",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ApplicationId": "application-xxxxxxx",
                    "ApplicationName": "test",
                    "ApplicationDesc": null,
                    "ApplicationType": "V",
                    "MicroserviceType": "N",
                    "ProgLang": null,
                    "CreateTime": null,
                    "UpdateTime": null
                }
            ]
        }
    }
}
```

