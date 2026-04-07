**Example 1: 修改广告插入配置**

修改广告插入配置

Input: 

```
tccli mps ModifyStreamPackageSSAIChannel --cli-unfold-argument  \
    --Name TestConf \
    --ContentSource http://origin-server.com/abc/ \
    --SSAIInfo.AdsUrl https://my.ads.com/path?ad_type=[player_params.ad_type]&region=[player_params.region] \
    --SSAIInfo.ConfigAliases.0.ParamName region \
    --SSAIInfo.ConfigAliases.0.AliasValueList.0.Alias india \
    --SSAIInfo.ConfigAliases.0.AliasValueList.0.Value ap-mumbai \
    --SSAIInfo.AdMarkerPassthrough True \
    --SSAIInfo.Threshold 12 \
    --SSAIInfo.SlateAd https://hostname/xxx/xxx.mp4 \
    --SSAIInfo.SCTE35AdType 1 \
    --SSAIInfo.AdTriggers 1 \
    --SSAIInfo.DeliveryRestrictions 1 \
    --SSAIInfo.SourceCDNPrefix https://example_cdn.com/ \
    --SSAIInfo.AdCDNPrefix https://example_ad_cdn.com/ \
    --ID 654CA8EF0000CE02BXXX
```

Output: 
```
{
    "Response": {
        "RequestId": "0xxxxd32-1043-4e1b-bd20-1bfad0xxxx70"
    }
}
```

