**Example 1: 获取人员库信息成功示例**



Input: 

```
tccli iai GetGroupInfo --cli-unfold-argument  \
    --GroupId 31
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

**Example 2: 获取人员库信息失败示例**



Input: 

```
tccli iai GetGroupInfo --cli-unfold-argument  \
    --GroupId 200
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人员库ID不存在。"
        },
        "RequestId": "0e77ad29-ad65-4901-9efc-b49a6e0a357b"
    }
}
```

