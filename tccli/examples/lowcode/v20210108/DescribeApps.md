**Example 1: 获取应用列表**

获取应用列表

Input: 

```
tccli lowcode DescribeApps --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --Favorite True
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "d2c7af0a-59a0-42aa-8f06-36888a27b6b1",
        "Weapps": [
            {
                "AppType": 1,
                "AttachAppId": "",
                "BackgroundColor": "",
                "Channel": "",
                "ClientId": "AAU5PwABBkwmrGD34LQ",
                "CmsProject": 0,
                "ContentType": "JSON",
                "CreateTime": "2023-03-03T10:16:18+08:00",
                "Description": "PC应用",
                "EData": "edata",
                "EType": 1,
                "Env": "{\"envId\": \"lowcode-1gisa8u9d5edc4f8\", \"region\": \"ap-shanghai\"}",
                "EnvId": "lowcode-1gisa8u9d5edc4f8",
                "EnvRegion": "ap-shanghai",
                "ExpireTime": "0001-01-01T00:00:00Z",
                "FaviconUrl": "",
                "FlowId": 0,
                "IconUrl": "",
                "Id": "app-1rdp4z6f",
                "IsFree": false,
                "JobInfo": {
                    "ErrMsg": "",
                    "Id": 0,
                    "Status": 0,
                    "Step": 0,
                    "StepDesc": "",
                    "TotalStep": 0
                },
                "LastDeployTime": "2025-02-21T14:45:03+08:00",
                "LastMpCiId": "",
                "LastMpCiMode": 0,
                "LastMpCiStatus": "",
                "LastWebCiId": "df352da2-f648-47ea-ae59-88df953eb550",
                "LastWebCiMode": 2,
                "LastWebCiStatus": "success",
                "Name": "app-1rdp4z6f",
                "Owner": "98528",
                "PkgId": "lowcode-1gisa8u9d5edc4f8",
                "Platform": "WEB",
                "SceneType": "",
                "Source": "",
                "Status": 0,
                "TemplateId": "",
                "Title": "资产管理",
                "UpdateTime": "2025-02-21T14:47:06+08:00",
                "Favorite": true,
                "PublishPlatform": "cloudAdmin"
            }
        ]
    }
}
```

