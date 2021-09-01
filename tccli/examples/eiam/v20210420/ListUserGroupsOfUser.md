**Example 1: 请求示例**



Input: 

```
tccli eiam ListUserGroupsOfUser --cli-unfold-argument  \
    --UserId 5c1ab60e-4844-4d92-8708-82257657d916
```

Output: 
```
{
    "Response": {
        "RequestId": "6cc65331-b49b-4bd3-b4da-3c1e5f598091",
        "UserId": "5c1ab60e-4844-4d92-8708-82257657d916",
        "UserGroupIds": [
            "1453013c-d0e9-424b-b9c7-dabcea3bd0ca"
        ]
    }
}
```

