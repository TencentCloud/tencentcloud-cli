**Example 1: 添加查询云应用版本信息请求**



Input: 

```
tccli car DescribeApplicationVersion --cli-unfold-argument  \
    --ApplicationId app-xlgehac
```

Output: 
```
{
    "Response": {
        "Versions": [
            {
                "ApplicationVersionId": "ver-uechqlx",
                "ApplicationVersionSize": 1024,
                "ApplicationVersionStatus": "Inuse",
                "ApplicationVersionName": "xxx",
                "CreateTime": "2021-08-29T08:00:30Z"
            }
        ],
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

