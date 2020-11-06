**Example 1: 调用失败示例**



Input: 

```
tccli bda GetGroupList --cli-unfold-argument  \
    --Offset -1 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "The value type of parameter `Offset` is not valid."
        },
        "RequestId": "78ec7830-a1c7-42be-bd65-6d0fa25f6fab"
    }
}
```

**Example 2: 调用成功示例**



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

