**Example 1: 查询日志**

查询http响应状态码（http_code）为200的日志

Input: 

```
tccli cls SearchLog --cli-unfold-argument  \
    --TopicId 601c2a87-ca8e-49c9-xxxx-27286a970db5 \
    --From 1679901909686 \
    --To 1679902809686 \
    --Query http_code:"200" \
    --Limit 1 \
    --Sort desc \
    --UseNewAnalysis True \
    --SyntaxRule 1
```

Output: 
```
{
    "Response": {
        "Context": "Y29udGV4dC0zZDVmZGI2NC1jNDZkLTQ2NzktYWM2OC1jYzg2NjUxYmVlMWExNjc5OTAyODEwNDM0",
        "ListOver": false,
        "Analysis": false,
        "ColNames": [],
        "Columns": null,
        "Results": [
            {
                "Time": 1679902806070,
                "TopicId": "601c2a87-ca8e-49c9-xxxx-27286a970db5",
                "TopicName": "CDN Demo访问日志日志主题_10000100xxxx",
                "Source": "",
                "FileName": "",
                "HostName": "",
                "PkgId": "",
                "PkgLogId": "",
                "LogJson": "{\"referer\":\"http://qwunsag.2022.qq.com/prizes?activity_code=AVGCHaQFX02Eb\",\"method\":\"GET\",\"isp\":\"中国联通\",\"remote_port\":\"45088\",\"ua\":\"Mozilla/5.0 (Linux; Android 9; INE-AL00 Build/HUAWEIINE-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/6389 MicroMessenger/8.0.11.1980(0x28000B5B) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64\",\"uuid\":\"acf1010c853f4a24bb3e92cc34e283e2\",\"version\":\"1\",\"file_size\":\"186358\",\"url\":\"/loxtxt/979884858.png\",\"request_range\":\"-\",\"rsp_size\":\"186830\",\"hit\":\"hit\",\"request_time\":\"2808\",\"http_code\":\"200\",\"param\":\"-\",\"sys_address\":\"9.130.154.208\",\"proto\":\"HTTPS\",\"host\":\"test.2022.cls.cn\",\"sys_datasource\":\"cq.3.4.v1.2.17\",\"client_ip\":\"116.116.247.167\",\"time\":\"1679902806070\",\"app_id\":\"1302700768\",\"prov\":\"内蒙古自治区\",\"timestamp\":\"2023-03-27T15:40:06+08:00\"}",
                "RawLog": "",
                "IndexStatus": ""
            }
        ],
        "AnalysisResults": [],
        "AnalysisRecords": null,
        "RequestId": "79f593e5-1374-4463-xxxx-c49d0b3c5290",
        "SamplingRate": 0,
        "Topics": null
    }
}
```

