**Example 1: 查询uin是否在白名单列表**



Input: 

```
tccli billing DescribeMeasureWhiteUinList --cli-unfold-argument  \
    --Interface.InterfaceName qcloud.yunapi.DescribeMeasureWhiteUinList \
    --Interface.Para.ProductCode p_ccc \
    --Interface.Para.Uin 123 \
    --RouteKey p_ccc
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsTestWhiteList": true,
            "Step": "1",
            "IsGrayscaleWhiteList": false
        },
        "RequestId": ""
    }
}
```

