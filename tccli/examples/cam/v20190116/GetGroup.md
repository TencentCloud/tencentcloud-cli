**Example 1: 查询用户组详情**



Input: 

```
tccli cam GetGroup --cli-unfold-argument  \
    --GroupId 2020
```

Output: 
```
{
    "Response": {
        "GroupId": 2020,
        "GroupName": "group1",
        "GroupNum": 1,
        "Remark": "IT",
        "CreateTime": "2019-04-03 15:11:34",
        "UserInfo": [
            {
                "Uid": 1001408,
                "Uin": 100000545998,
                "Name": "zhangsan",
                "PhoneNum": "188****8888",
                "CountryCode": "86",
                "PhoneFlag": 0,
                "Email": "user1***@tencent.com",
                "EmailFlag": 0,
                "UserType": 3,
                "CreateTime": "2018-04-24 15:36:26",
                "IsReceiverOwner": 0
            }
        ],
        "RequestId": "4a00d281-862a-4699-9d71-387d9fc2c36a"
    }
}
```

