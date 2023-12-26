**Example 1: 获取会员信息**

获取会员信息

Input: 

```
tccli yinsuda DescribeVipUserInfo --cli-unfold-argument  \
    --AppName test \
    --UserId James
```

Output: 
```
{
    "Response": {
        "AnchorId": "James",
        "EndTime": "2023-12-28 11:53:47",
        "IsVip": 1,
        "RequestId": "75d1a921-a3c1-4cdf-9834-b9eef2130bc0",
        "RoomId": "123",
        "Status": 1
    }
}
```

