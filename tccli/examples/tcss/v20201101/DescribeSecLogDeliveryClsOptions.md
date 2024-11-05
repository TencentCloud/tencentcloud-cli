**Example 1: 查询安全日志投递cls可选项**



Input: 

```
tccli tcss DescribeSecLogDeliveryClsOptions --cli-unfold-argument  \
    --ClsRegion ap-bangkok
```

Output: 
```
{
    "Response": {
        "LogSetList": [],
        "RegionList": [
            {
                "Region": "ap-bangkok",
                "RegionName": "亚太东南(曼谷)"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "华北地区(北京)"
            },
            {
                "Region": "ap-chengdu",
                "RegionName": "西南地区(成都)"
            }
        ],
        "RequestId": "31c5ca59-2ed8-4b22-8ebf-6ba5003caea3"
    }
}
```

