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
                    "ApplicationId": "abc",
                    "ApplicationName": "abc",
                    "ApplicationType": "abc",
                    "MicroserviceType": "abc",
                    "ApplicationDesc": "abc",
                    "ProgLang": "abc",
                    "ApplicationResourceType": "abc",
                    "CreateTime": "abc",
                    "UpdateTime": "abc",
                    "ApigatewayServiceId": "abc",
                    "ApplicationRuntimeType": "abc",
                    "AmpInstanceId": "abc",
                    "ApmInstanceName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

