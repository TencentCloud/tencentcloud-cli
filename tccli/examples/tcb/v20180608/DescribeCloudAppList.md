**Example 1: 查询云应用列表**



Input: 

```
tccli tcb DescribeCloudAppList --cli-unfold-argument  \
    --EnvId l******-******53798f7294 \
    --DeployType static-hosting \
    --PageSize 1 \
    --PageNo 1
```

Output: 
```
{
    "Response": {
        "ServiceList": [
            {
                "AppPath": "/React_New_TestT",
                "CreateTime": "2026-05-29 10:58:46",
                "DeployType": "static-hosting",
                "Domain": "****************************************.webapps.tcloudbase.com",
                "Framework": "react",
                "LatestBuildTime": "2026-05-29 10:58:46",
                "LatestStatus": "SUCCESS",
                "LatestVersionName": "React_New_TestT-001",
                "ServiceName": "React_New_TestT"
            }
        ],
        "Total": 6,
        "RequestId": "6f480c2b-7a8a-46e6-8207-09c472e70466"
    }
}
```

