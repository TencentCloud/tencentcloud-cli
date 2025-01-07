**Example 1: 获取应用配置**

获取应用配置

Input: 

```
tccli lcic DescribeAppDetail --cli-unfold-argument  \
    --ApplicationId 3028839 \
    --DeveloperId db5bb499-8691-463f-ac64-1a48f80d968a
```

Output: 
```
{
    "Response": {
        "SdkAppId": "13465287",
        "AppConfig": {
            "ApplicationId": "2CvDgjRNjylAs",
            "AppName": "appName01",
            "State": 0,
            "AppVersion": 0,
            "CreatedAt": "1704074400",
            "Callback": "http://11.22.33.44:8080/callback",
            "CallbackKey": "myCallBack"
        },
        "SceneConfig": [
            {
                "Scene": "scene01",
                "LogoUrl": "http://11.22.33.44:8080/log",
                "HomeUrl": "http://11.22.33.44:8080/home",
                "JSUrl": "http://11.22.33.44:8080/js",
                "CSSUrl": "http://11.22.33.44:8080/css"
            }
        ],
        "TransferConfig": {
            "State": 1
        },
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

