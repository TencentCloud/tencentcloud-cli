**Example 1: 创建SSAI广告插入配置**

创建SSAI广告插入配置

Input: 

```
tccli mps CreateStreamPackageSSAIChannel --cli-unfold-argument  \
    --Name TestConf \
    --ContentSource https://www.tencent.com/abc \
    --SSAIInfo.AdsUrl https://www.tencent.com/abc \
    --SSAIInfo.ConfigAliases.0.ParamName region \
    --SSAIInfo.ConfigAliases.0.AliasValueList.0.Alias india \
    --SSAIInfo.ConfigAliases.0.AliasValueList.0.Value ap-mumbai \
    --SSAIInfo.AdMarkerPassthrough True \
    --SSAIInfo.SCTE35AdType 1 \
    --SSAIInfo.SlateAd https://www.tencent.com/abc.mp4 \
    --SSAIInfo.Threshold 12 \
    --SSAIInfo.DashMPDLocation True \
    --SSAIInfo.AdTriggers 1 \
    --SSAIInfo.DeliveryRestrictions 1 \
    --SSAIInfo.SourceCDNPrefix https://www.tencent.com/abc \
    --SSAIInfo.AdCDNPrefix https://www.tencent.com/abc \
    --SSAIInfo.PreRollAdsUrl https://www.tencent.com/abc \
    --SSAIInfo.PreRollMaxAllowedDuration 30 \
    --SSAIInfo.MultiRequest True
```

Output: 
```
{
    "Response": {
        "Info": {
            "ContentSource": "https://www.tencent.com/abc",
            "ID": "698AAD421D3EA5656115",
            "Name": "TestConf",
            "PlaybackPrefix": "http://xxx.a*-mumbai.streampackage.s*************qcloud.com/v1/ssai/m***er/**94d961674a1eb4611d3xxxxx**",
            "Region": "ap-shanghai",
            "SSAIInfo": {
                "AdCDNPrefix": "https://www.tencent.com/abc",
                "AdMarkerPassthrough": true,
                "AdTriggers": [
                    1
                ],
                "AdsUrl": "https://www.tencent.com/abc",
                "ConfigAliases": [
                    {
                        "AliasValueList": [
                            {
                                "Alias": "india",
                                "Value": "ap-mumbai"
                            }
                        ],
                        "ParamName": "region"
                    }
                ],
                "DashMPDLocation": false,
                "DeliveryRestrictions": 1,
                "MultiRequest": true,
                "PreRollAdsUrl": "https://www.tencent.com/abc",
                "PreRollMaxAllowedDuration": 30,
                "SCTE35AdType": 1,
                "SlateAd": "https://www.tencent.com/abc.mp4",
                "SourceCDNPrefix": "https://www.tencent.com/abc",
                "Threshold": 12
            },
            "SessionInitPrefix": "http://251***5**.ap-s******i.stream******e***clivepull.myqcloud.*om/v**ssai/session/019c45b4c9121500****34b5a3c17/"
        },
        "RequestId": "cf3cc57b-2091-4061-b120-ec950d913412"
    }
}
```

