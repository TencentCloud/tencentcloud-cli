**Example 1: 获取人员库信息**



Input: 

```
tccli iai GetGroupInfo --cli-unfold-argument  \
    --GroupId "31"
```

Output: 
```
{
    "Response": {
        "GroupName": "人员库",
        "GroupId": "31",
        "GroupExDescriptions": [
            "年龄"
        ],
        "Tag": "不含实习生",
        "FaceModelVersion": "3.0",
        "CreationTimestamp": 1559530931613,
        "RequestId": "6faa05d0-287b-464e-8755-cf3e8d0c703d"
    }
}
```

