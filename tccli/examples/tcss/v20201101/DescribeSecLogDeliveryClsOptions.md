**Example 1: 查询安全日志投递cls可选项**



Input: 

```
tccli tcss DescribeSecLogDeliveryClsOptions --cli-unfold-argument  \
    --ClsRegion 
```

Output: 
```
{
    "Response": {
        "LogSetList": [
            {
                "LogsetName": "xx",
                "TopicList": [
                    {
                        "TopicName": "xx",
                        "TopicID": "xx"
                    }
                ],
                "LogsetID": "xx"
            }
        ],
        "RegionList": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州"
            }
        ],
        "RequestId": "xx"
    }
}
```

