**Example 1: 查询子客信息**

查询子客信息

Input: 

```
tccli intlpartnersmgt DescribeCustomerInfo --cli-unfold-argument  \
    --CustomerUin 200000000000 200000000001 200000000002
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CustomerUin": "200000000000",
                "Email": "test@gmail.com",
                "Phone": "18888888",
                "Mark": "for test",
                "Name": "tom",
                "BindTime": "2020-01-01 08:00:00",
                "AccountStatus": "0",
                "AuthStatus": "0"
            }
        ],
        "RequestId": "91991903-****-42ca-9f0d-68****39b231"
    }
}
```

