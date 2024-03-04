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
        "SdkAppId": "abc",
        "AppConfig": {
            "ApplicationId": "abc",
            "AppName": "abc",
            "State": 0,
            "AppVersion": 0,
            "CreatedAt": "abc",
            "Callback": "abc",
            "CallbackKey": "abc"
        },
        "SceneConfig": [
            {
                "Scene": "abc",
                "LogoUrl": "abc",
                "HomeUrl": "abc",
                "JSUrl": "abc",
                "CSSUrl": "abc"
            }
        ],
        "TransferConfig": {
            "State": 1
        },
        "RequestId": "abc"
    }
}
```

