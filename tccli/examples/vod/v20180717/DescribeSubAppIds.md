**Example 1: Querying subapplication resource list**



Input: 

```
tccli vod DescribeSubAppIds --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SubAppIdInfoSet": [
            {
                "SubAppId": 1451123904,
                "Name": "Subapplication 1",
                "Description": "Overview of subapplication 1",
                "CreateTime": "2018-10-01T10:00:00Z",
                "Status": "On"
            },
            {
                "SubAppId": 1251123904,
                "Name": "Primary application",
                "Description": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "Status": "On"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

