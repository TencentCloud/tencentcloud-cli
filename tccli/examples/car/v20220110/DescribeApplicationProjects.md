**Example 1: 获取云应用项目列表**



Input: 

```
tccli car DescribeApplicationProjects --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "Projects": [
            {
                "IsPreload": true,
                "Description": "app",
                "ProjectId": "cap-a1b2c3",
                "ApplicationStatus": "NoConcurrent",
                "ApplicationName": "abc",
                "Resolution": "1920x1080",
                "ProjectType": "SHARED",
                "Purpose": "EXPERIENCE",
                "Amount": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "Using": 0,
                "ApplicationId": "app-a1b2c3",
                "Type": "XL2",
                "ApplicationParams": "",
                "Name": "",
                "ApplicationRegions": [
                    "ap-chinese-mainland",
                    "na-north-america-fusion"
                ],
                "ConcurrentRegions": [
                    "ap-chinese-mainland",
                    "na-north-america-fusion"
                ]
            }
        ],
        "Total": 0
    }
}
```

