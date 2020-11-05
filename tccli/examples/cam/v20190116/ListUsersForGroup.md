**Example 1: Querying the List of Users Associated with a User Group**



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

