**Example 1: 获取直播源站配置信息**



Input: 

```
tccli live DescribeOriginStreamInfo --cli-unfold-argument  \
    --DomainName autotest-third-source01.elementtest.org
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "DomainName": "autotest-third-source01.elementtest.org",
        "CdnStreamPlayType": [
            "rtmp",
            "hls",
            "flv"
        ],
        "OriginStreamType": 1,
        "OriginStreamPlayType": "rtmp",
        "OriginAddressType": 1,
        "OriginAddress": [
            "60.215.15.235:1935",
            "32.16.116.191:1935"
        ],
        "OriginTimeout": 10000,
        "OriginRetryTimes": 10,
        "TimeJitter": "off",
        "HlsPlayFragmentCount": 3,
        "HlsPlayFragmentDuration": 3000,
        "PassThroughHttpHeader": "off",
        "PassThroughResponse": "off",
        "PassThroughParam": "off",
        "OriginHost": null,
        "IndexerCache": null,
        "FragmentCache": null,
        "UsingHttps": "off",
        "CacheFollowOrigin": "off",
        "CacheStatusCode": [],
        "UrlReplaceRules": [],
        "OptionsRequest": "off",
        "FollowRedirect": "on",
        "CustomerName": null,
        "StreamPackageRegion": null,
        "IndexerKeepParam": [],
        "FragmentKeepParam": [],
        "MediaPackageType": null,
        "IndexerHeader": [],
        "FragmentHeader": [],
        "RequestId": "85f82143-b8a2-467c-bcff-6729fd7a471f"
    }
}
```

