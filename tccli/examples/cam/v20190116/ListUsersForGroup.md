**Example 1: 查询用户组关联的用户列表**



Input: 

```
tccli cam ListUsersForGroup --cli-unfold-argument  \
    --GroupId 2020
```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "UserInfo": [
            {
                "Uid": 1001408,
                "Uin": 100000545998,
                "Name": "testName",
                "PhoneNum": "",
                "CountryCode": "86",
                "PhoneFlag": 0,
                "Email": "",
                "EmailFlag": 0,
                "UserType": 3,
                "CreateTime": "2018-04-24 15:36:26",
                "IsReceiverOwner": 0
            }
        ],
        "RequestId": "576e68f4-49cf-451b-b717-a584cb68910a"
    }
}
```

