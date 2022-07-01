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
        "EvilType": 268,
        "Level": 5,
        "UrlTypeDesc": "黑",
        "EvilClassDesc": "非法内容（根据法律法规不能传播的内容，主要为政治敏感内容，默认内部使用）",
        "EvilTypeDesc": "色情网站(网信办)",
        "LevelDesc": "整域",
        "DetectTime": 1644834245,
        "Wording": "该网站发布了违反国家相关法律规定的内容，已为您拦截。",
        "WordingTitle": "该网站可能存在非法内容"
    }
}
```

