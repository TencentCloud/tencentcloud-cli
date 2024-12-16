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
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "ApplicationId": "application-6a79x94v",
                    "ApplicationName": "app-mock",
                    "ApplicationType": "C",
                    "MicroserviceType": "DEF",
                    "ApplicationDesc": "this is a desc",
                    "ProgLang": "J",
                    "ApplicationResourceType": "DEF",
                    "CreateTime": "2019-11-22 11:12:22",
                    "UpdateTime": "2019-11-22 11:12:22",
                    "ApigatewayServiceId": "gw-ins-6a79x94v",
                    "ApplicationRuntimeType": "konaJdk8",
                    "AmpInstanceId": "apm-6a79x94v",
                    "ApmInstanceName": "apm-mock"
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

