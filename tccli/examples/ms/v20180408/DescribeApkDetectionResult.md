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
        "Reason": "xx",
        "ResultList": [
            {
                "SafeType": "xx",
                "BoutiqueRecommand": "xx",
                "OptPluginList": [
                    {
                        "PluginDesc": "xx",
                        "PluginName": "xx",
                        "PluginType": "xx"
                    }
                ],
                "Sid": "xx",
                "VirusDesc": "xx",
                "Official": "xx",
                "Spot": "xx",
                "Errno": "xx",
                "SoftName": "xx",
                "RepackageStatus": "xx",
                "PluginList": [
                    {
                        "PluginDesc": "xx",
                        "PluginName": "xx",
                        "PluginType": "xx"
                    }
                ],
                "IntegralWall": "xx",
                "NotifyBar": "xx",
                "FloatWindows": "xx",
                "Md5": "xx",
                "Banner": "xx",
                "ErrMsg": "xx",
                "VirusName": "xx"
            }
        ],
        "RequestId": "xx",
        "Result": "xx"
    }
}
```

