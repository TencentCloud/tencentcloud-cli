**Example 1: 获取群组成员列表**

获取群组成员列表

Input: 

```
tccli lcic DescribeGroupMemberList --cli-unfold-argument  \
    --GroupId abcdfdfg \
    --SdkAppId 12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "213das",
        "Total": 2,
        "MemberIds": [
            "dfgdfgd",
            "dfgsdfg"
        ]
    }
}
```

