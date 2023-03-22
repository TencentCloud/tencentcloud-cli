**Example 1: 查询子应用资源列表**

查询子应用资源列表

Input: 

```
tccli vod DescribeSubAppIds --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "SubAppIdInfoSet": [
            {
                "SubAppId": 1451123904,
                "Name": "子应用1",
                "SubAppIdName": "主应用",
                "Description": "子应用1简介",
                "CreateTime": "2018-10-01T10:00:00Z",
                "Status": "On"
            },
            {
                "SubAppId": 1251123904,
                "Name": "主应用",
                "SubAppIdName": "主应用",
                "Description": "",
                "CreateTime": "2018-10-01T10:00:00Z",
                "Status": "On"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

