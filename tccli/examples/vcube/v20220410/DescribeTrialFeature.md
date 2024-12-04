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
                "Id": 1,
                "FeatureId": 1,
                "Name": "abc",
                "Type": "abc",
                "Trial": true,
                "TrialCount": 1,
                "Duration": 1,
                "CreatedAt": "abc",
                "UpdatedAt": "abc"
            }
        ],
        "XMagicTrial": {
            "Name": "abc",
            "TrialCount": 1,
            "Duration": 1,
            "Plan": "abc",
            "XMagicType": "abc"
        },
        "XMagicTrialList": [
            {
                "Name": "abc",
                "TrialCount": 1,
                "Duration": 1,
                "Plan": "abc",
                "XMagicType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

