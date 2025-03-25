**Example 1: 查询测试应用可以开通的功能**

查询测试应用可以开通的功能

Input: 

```
tccli vcube DescribeTrialFeature --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FeatureList": [
            {
                "CreatedAt": "2021-08-09T03:29:19.404Z",
                "Duration": 14,
                "FeatureId": 3,
                "Id": 2,
                "Name": "短视频基础版",
                "Trial": true,
                "TrialCount": 2,
                "Type": "短视频制作基础版+视频播放",
                "UpdatedAt": "2023-11-09T06:32:36.000Z"
            }
        ],
        "XMagicTrial": {
            "Duration": 0,
            "Name": "高级套餐S1-04",
            "Plan": "S1-04",
            "TrialCount": 0,
            "XMagicType": "combined"
        },
        "XMagicTrialList": [
            {
                "Duration": 0,
                "Name": "高级套餐S1-04",
                "Plan": "S1-04",
                "TrialCount": 0,
                "XMagicType": "combined"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

