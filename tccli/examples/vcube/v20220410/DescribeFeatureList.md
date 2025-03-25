**Example 1: 查询功能列表**

查询功能列表

Input: 

```
tccli vcube DescribeFeatureList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FeatureList": [
            {
                "BizType": "vod",
                "CreatedAt": "2021-08-09T03:28:41.000Z",
                "Duration": 14,
                "FeatureId": 2,
                "Id": 1,
                "Name": "短视频精简版",
                "Platform": "mobile",
                "Trial": false,
                "TrialCount": 2,
                "Type": "短视频制作精简版+视频播放",
                "UpdatedAt": "2023-11-09T06:26:40.000Z"
            }
        ],
        "RequestId": "8fa791da-e6f6-4f70-9538-72e8fe0ad49d",
        "XMagicFeatureList": [
            {
                "BizType": "xmagic",
                "Duration": 14,
                "Name": "基础套餐A1-00",
                "Plan": "A1-00",
                "Trial": false,
                "TrialCount": 2,
                "XMagicType": "combined"
            }
        ]
    }
}
```

