**Example 1: 请求示例**



Input: 

```
tccli eiam AddUserToUserGroup --cli-unfold-argument  \
    --UserIds 3945dcb0-e433-****-a69b-b5074abe3cbd 5c1ab60e-4844-****-8708-82257657d916 df68819a-804b-****-af68-682b28d5c02e \
    --UserGroupId 1453013c-****-424b-b9c7-dabcea3bd0ca
```

Output: 
```
{
    "Response": {
        "RequestId": "424b-804b-****-af68-682b28d5c02e",
        "FailedItems": [
            "5c1ab60e-4844-****-8708-82257657d916"
        ]
    }
}
```

