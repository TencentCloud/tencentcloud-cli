**Example 1: DescribeLatestRelease**



Input: 

```
tccli adp DescribeLatestRelease --cli-unfold-argument  \
    --AppId 206************5184
```

Output: 
```
{
    "Response": {
        "IsChanged": false,
        "ReleaseSummary": {
            "ChannelIdList": [],
            "CreateTime": "1780389728",
            "Description": "我的发布信息",
            "ReleaseId": "2061***********7232",
            "Status": 3,
            "StatusDescription": "发布成功"
        },
        "RequestId": "0db8ec29-fb0f-45a3-8067-57206b475d1b"
    }
}
```

