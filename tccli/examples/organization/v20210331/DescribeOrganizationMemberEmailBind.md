**Example 1: 查询成员邮箱绑定详细信息**



Input: 

```
tccli organization DescribeOrganizationMemberEmailBind --cli-unfold-argument  \
    --MemberUin 123
```

Output: 
```
{
    "Response": {
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957",
        "BindId": 1,
        "ApplyTime": "2022-01-13 12:09:08",
        "Email": "123@qq.com",
        "Phone": "18798765432",
        "BindStatus": "Success",
        "BindTime": "2022-01-13 18:09:08",
        "Description": "",
        "PhoneBind": 0,
        "CountryCode": "86"
    }
}
```

