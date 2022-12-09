**Example 1: 查询网址检测结果服务**



Input: 

```
tccli ms DescribeUrlDetectionResult --cli-unfold-argument  \
    --Url http://17biquge.com
```

Output: 
```
{
    "Response": {
        "RequestId": "c2adb7ea-3f73-487a-8ea5-474277c29e3a",
        "ResultCode": 0,
        "RespVer": 1,
        "UrlType": 2,
        "EvilClass": 8,
        "EvilType": 0,
        "Level": 0,
        "UrlTypeDesc": "风险网址",
        "EvilClassDesc": "",
        "EvilTypeDesc": "",
        "LevelDesc": "",
        "DetectTime": 1644834245,
        "Wording": "",
        "WordingTitle": ""
    }
}
```

