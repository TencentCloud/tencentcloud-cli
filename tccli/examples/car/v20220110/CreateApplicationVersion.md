**Example 1: 添加创建云应用版本请求**



Input: 

```
tccli car CreateApplicationVersion --cli-unfold-argument  \
    --ApplicationId xxx \
    --ApplicationFileName xxx.zip
```

Output: 
```
{
    "Response": {
        "Version": {
            "ApplicationVersionId": "app-efgtyab",
            "ApplicationVersionSize": 1024,
            "ApplicationVersionStatus": "Creating",
            "ApplicationVersionName": "xxx",
            "CreateTime": "2020-09-22T00:00:00+00:00"
        },
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

