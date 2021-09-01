**Example 1: 获取已购曲库包列表**

获取已购曲库包列表

Input: 

```
tccli ame DescribePackages --cli-unfold-argument  \
    --Offset 0 \
    --Length 20
```

Output: 
```
{
    "Response": {
        "Packages": [
            {
                "AuthorizedArea": "CN",
                "AuthorizedLimit": 2000,
                "Commercial": 0,
                "EffectTime": "2020-07-03 16:05:01",
                "ExpireTime": "2021-07-03 16:05:01",
                "Name": "商用通用-在线",
                "OrderId": "10070316050031100",
                "PackagePrice": 200000,
                "TermOfValidity": 365,
                "UseRanges": [
                    {
                        "Name": "API音乐使用场景/短视频背景音（免费）",
                        "UseRangeId": 32
                    },
                    {
                        "Name": "API音乐使用场景/图文背景音（免费）",
                        "UseRangeId": 33
                    },
                    {
                        "Name": "API音乐使用场景/应用程序背景音（免费）",
                        "UseRangeId": 34
                    },
                    {
                        "Name": "API音乐使用场景/网页/个人空间背景音乐定制（付费）",
                        "UseRangeId": 1005
                    },
                    {
                        "Name": "API音乐使用场景/客户端背景音乐内置（付费）",
                        "UseRangeId": 1008
                    },
                    {
                        "Name": "API音乐使用场景/视频背景音乐（付费）",
                        "UseRangeId": 1013
                    }
                ],
                "UsedCount": 10
            }
        ],
        "RequestId": "s1596075862723742000"
    }
}
```

