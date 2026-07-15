**Example 1: DescribeReleaseSummary**



Input: 

```
tccli adp DescribeReleaseSummary --cli-unfold-argument  \
    --AppId 2060************184 \
    --ReleaseId 2060***********3392
```

Output: 
```
{
    "Response": {
        "ReleaseSummary": {
            "ChannelIdList": [],
            "CreateTime": "1780045630",
            "Description": "",
            "ReleaseId": "2060***********3392",
            "Status": 3,
            "StatusDescription": "发布成功"
        },
        "RequestId": "f3052ff0-4b3f-40a8-ba05-5c2019a909c6"
    }
}
```

