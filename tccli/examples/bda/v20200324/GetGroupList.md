**Example 1: 调用成功示例**



Input: 

```
tccli bda GetGroupList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "GroupNum": 1,
        "GroupInfos": [
            {
                "GroupName": "testG2",
                "GroupId": "testG2",
                "Tag": "testG2Tag",
                "BodyModelVersion": "1.0",
                "CreationTimestamp": 1581673977535
            }
        ],
        "RequestId": "9ffccff2-4b52-443f-98f4-eb1f6a30399e"
    }
}
```

