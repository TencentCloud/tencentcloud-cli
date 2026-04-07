**Example 1: 批量查询广告插入配置**

批量查询广告插入配置

Input: 

```
tccli mps DescribeStreamPackageSSAIChannels --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "ID": "654CA8EF0000CE02BXXX",
                "Name": "TestConf",
                "ContentSource": "http://origin-server.com/abc/",
                "PlaybackPrefix": "http://xxx.ap-mumbai.streampackage.srclivepull.myqcloud.com/v1/ssai/master/0194d961674a1eb4611d3xxxxxx/",
                "SSAIInfo": {
                    "AdsUrl": "https://my.ads.com/path?ad_type=[player_params.ad_type]&region=[player_params.region]",
                    "ConfigAliases": [
                        {
                            "ParamName": "region",
                            "AliasValueList": [
                                {
                                    "Alias": "india",
                                    "Value": "ap-mumbai"
                                }
                            ]
                        }
                    ],
                    "AdMarkerPassthrough": true,
                    "Threshold": 12,
                    "SlateAd": "https://hostname/xxx/xxx.mp4",
                    "SCTE35AdType": 1,
                    "AdTriggers": [
                        1
                    ],
                    "DeliveryRestrictions": 1,
                    "SourceCDNPrefix": "https://example_cdn.com/",
                    "AdCDNPrefix": "https://example_ad_cdn.com/",
                    "DashMPDLocation": false
                }
            }
        ],
        "PageNum": 1,
        "PageSize": 1,
        "TotalNum": 1,
        "RequestId": "0xxxxd32-1043-4e1b-bd20-1bfad0xxxx70"
    }
}
```

