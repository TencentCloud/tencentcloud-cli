**Example 1: 查询子应用白名单配置**



Input: 

```
tccli vod DescribeAigcWhitelist --cli-unfold-argument  \
    --SubAppId 200000 \
    --AigcType Video
```

Output: 
```
{
    "Response": {
        "AigcType": "Video",
        "IpWhitelist": [
            "4*.*.*.0/8"
        ],
        "IpWhitelistSwitch": "ON",
        "ModelWhitelist": [
            {
                "ModelName": "Hunyuan",
                "ModelVersion": "1.5"
            }
        ],
        "ModelWhitelistSwitch": "ON",
        "RequestId": "4bb3588f-18a6-4caa-a667-096f13498afa"
    }
}
```

