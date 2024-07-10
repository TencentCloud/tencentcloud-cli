**Example 1: 示例1**



Input: 

```
tccli mna GetGroupList --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1 \
    --Keyword test
```

Output: 
```
{
    "Response": {
        "GroupInfos": [
            {
                "GroupId": "abc",
                "GroupName": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Description": "abc",
                "DeviceNum": 5
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

