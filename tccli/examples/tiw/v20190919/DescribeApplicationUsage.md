**Example 1: 查询白板用量**

按天查询白板用量

Input: 

```
tccli tiw DescribeApplicationUsage --cli-unfold-argument  \
    --TimeLevel DAILY \
    --SubProduct sp_tiw_ric \
    --BeginTime 2019-10-01 00:00:00 \
    --SdkAppId 1400000001 \
    --IsWeighted True \
    --EndTime 2019-12-31 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Details": [
                    {
                        "Value": 0.1,
                        "Weight": 0.1,
                        "TagName": "tag_name"
                    }
                ],
                "Value": 23773611121,
                "Time": "2019-11-10 00:00:00"
            }
        ],
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

