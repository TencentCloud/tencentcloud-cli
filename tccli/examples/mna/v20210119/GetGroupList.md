**Example 1: 示例1**



Input: 

```
tccli mna GetGroupList --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1 \
    --Keyword Keyword
```

Output: 
```
{
    "Response": {
        "GroupInfos": [
            {
                "GroupId": "group-id1",
                "GroupName": "gname",
                "CreateTime": "1734401551",
                "UpdateTime": "1734401551",
                "Description": "GetGroupList描述",
                "DeviceNum": 5
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "a1434e98-16e8-41de-9b9b-27805a9cffbf"
    }
}
```

