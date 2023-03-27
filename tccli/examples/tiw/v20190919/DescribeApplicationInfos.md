**Example 1: 查询白板应用列表**

查询白板应用列表

Input: 

```
tccli tiw DescribeApplicationInfos --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ApplicationInfos": [
            {
                "TagList": [
                    {
                        "TagKey": "tag_key",
                        "TagValue": "tag_value"
                    }
                ],
                "SdkAppId": "1400000001",
                "AppName": "ForTest",
                "CreateTime": "2019-11-10 00:00:00"
            }
        ],
        "AllOption": 1,
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

