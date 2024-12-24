**Example 1: 添加创建云应用版本请求**



Input: 

```
tccli car CreateApplicationVersion --cli-unfold-argument  \
    --ApplicationId app-a1b2c3d4 \
    --ApplicationFileName test.zip \
    --ApplicationVersionRegions ap-chinese-mainland na-north-america-fusion \
    --ApplicationVersionUpdateMode FULL
```

Output: 
```
{
    "Response": {
        "Version": {
            "ApplicationVersionId": "ver-ug59y45y",
            "ApplicationVersionName": "test",
            "ApplicationVersionRegions": [
                "ap-chinese-mainland"
            ],
            "ApplicationVersionSize": 0,
            "ApplicationVersionStatus": "Creating",
            "ApplicationVersionUpdateMode": "FULL",
            "CreateTime": "2024-12-23T11:13:55Z"
        },
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

