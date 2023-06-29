**Example 1: 获取应用配置**

获取应用配置

Input: 

```
tccli lcic DescribeAppDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppConfig": {
            "AppName": "123",
            "AppVersion": 4,
            "ApplicationId": "3028839",
            "Callback": "",
            "CallbackKey": "dddd",
            "CreatedAt": "2022-10-26 16:45:02",
            "Introduce": "",
            "PostPaid": 1,
            "State": 1,
            "Tags": []
        },
        "RequestId": "9dfae8e8a8c5e4b27b7abf37caa2e5bf",
        "SceneConfig": [
            {
                "CSSUrl": "https://tcic-test-1257307760.file.myqcloud.com/customcontent/1079976/default_custom.css",
                "HomeUrl": "https://class.qcloudtiw.com/login.html",
                "JSUrl": "https://tcic-test-1257307760.file.myqcloud.com/customcontent/1079976/default_custom.js",
                "LogoUrl": "https://tcic-test-1257307760.file.myqcloud.com/customcontent/1079976/default_77fe1a555c64762691cb83ef20fe2a1e.png",
                "Scene": "dev"
            }
        ],
        "SdkAppId": "1400315010"
    }
}
```

