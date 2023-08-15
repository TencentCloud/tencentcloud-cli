**Example 1: 结束房间**

房间ID存在示例

Input: 

```
tccli lcic EndRoom --cli-unfold-argument  \
    --RoomId 1111
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.Room",
            "Message": "The room does not exist."
        },
        "RequestId": "19faa0a4-c1c8-40fe-afdb-6cb67f1b3196"
    }
}
```

