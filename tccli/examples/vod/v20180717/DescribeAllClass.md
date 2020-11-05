**Example 1: Getting video category hierarchy**



Input: 

```
tccli vod DescribeAllClass --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ClassInfoSet": [
            {
                "ClassId": 0,
                "Level": 0,
                "ClassName": "Other",
                "ParentId": -1,
                "SubClassIdSet": null
            },
            {
                "ClassId": 1,
                "Level": 0,
                "ClassName": "Custom first-level category",
                "ParentId": -1,
                "SubClassIdSet": [
                    2,
                    3
                ]
            },
            {
                "ClassId": 2,
                "Level": 2,
                "ClassName": "Custom second-level category",
                "ParentId": 1,
                "SubClassIdSet": [
                    4,
                    5
                ]
            },
            {
                "ClassId": 3,
                "Level": 2,
                "ClassName": "Custom second-level category",
                "ParentId": 1,
                "SubClassIdSet": null
            },
            {
                "ClassId": 4,
                "Level": 3,
                "ClassName": "Custom third-level category",
                "ParentId": 2,
                "SubClassIdSet": null
            },
            {
                "ClassId": 5,
                "Level": 3,
                "ClassName": "Custom third-level category",
                "ParentId": 2,
                "SubClassIdSet": null
            }
        ],
        "RequestId": "requestId"
    }
}
```

