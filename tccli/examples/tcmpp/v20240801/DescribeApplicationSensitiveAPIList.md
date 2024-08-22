**Example 1: DescribeApplicationSensitiveAPIList**



Input: 

```
tccli tcmpp DescribeApplicationSensitiveAPIList --cli-unfold-argument  \
    --Limit 30 \
    --Offset 0 \
    --Keyword testState \
    --ApplicationId app-cc6g35711m \
    --TeamId 3686677859 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "DataList": [
                {
                    "APIId": "api-rj2b08c8cang07nb",
                    "APIName": "testState",
                    "APIMethod": "testState",
                    "APIDesc": "testState",
                    "ApplicationId": "app-cc6g35711m",
                    "ApplicationName": "autotest_app",
                    "ApplicationLogo": "https://127.0.0.1/T04257DS9431720WTAG/console/20240802112441-cf9ba6bd4c.png",
                    "TeamId": "3686677859",
                    "TeamName": "autotest_app_team",
                    "CreateUser": "800001208871",
                    "CreateTime": "1724245061",
                    "UpdateUser": "800001208871",
                    "UpdateTime": "1724245061",
                    "APIType": 2,
                    "Status": 0
                }
            ]
        },
        "RequestId": "66d355a2-7ece-49ce-acf0-1ec070da324b"
    }
}
```

