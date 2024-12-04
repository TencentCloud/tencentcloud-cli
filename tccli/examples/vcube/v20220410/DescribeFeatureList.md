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
        "XMagicFeatureList": [
            {
                "Name": "abc",
                "TrialCount": 1,
                "Duration": 1,
                "Plan": "abc",
                "XMagicType": "abc",
                "Trial": true,
                "BizType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

