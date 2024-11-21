**Example 1: 环境安全检测-apk检测**



Input: 

```
tccli ms DescribeApkDetectionResult --cli-unfold-argument  \
    --ApkUrl http://xxx.xxx \
    --ApkMd5 2751xxxxxd1d203d6621ea28a0axxxxx
```

Output: 
```
{
    "Response": {
        "Reason": "success",
        "ResultList": [
            {
                "SafeType": "1",
                "BoutiqueRecommand": "1",
                "OptPluginList": [
                    {
                        "PluginDesc": "非广告插件描述",
                        "PluginName": "非广告插件名称",
                        "PluginType": "1"
                    }
                ],
                "Sid": "sid-xxxxxx",
                "VirusDesc": "病毒描述",
                "Official": "1",
                "Spot": "0",
                "Errno": "0",
                "SoftName": "安装包名称",
                "RepackageStatus": "0",
                "PluginList": [
                    {
                        "PluginDesc": "广告插件描述",
                        "PluginName": "广告插件名称",
                        "PluginType": "1"
                    }
                ],
                "IntegralWall": "1",
                "NotifyBar": "1",
                "FloatWindows": "1",
                "Md5": "8c7ef86c259abad33f213405a35a13c2",
                "Banner": "0",
                "ErrMsg": "success",
                "VirusName": "病毒名称"
            }
        ],
        "RequestId": "RequestId-xxxxx",
        "Result": "Result-xxxxx"
    }
}
```

