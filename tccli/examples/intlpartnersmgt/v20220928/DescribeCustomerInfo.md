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
                "CustomerUin": "abc",
                "Email": "abc",
                "Phone": "abc",
                "Mark": "abc",
                "Name": "abc",
                "BindTime": "abc",
                "AccountStatus": "abc",
                "AuthStatus": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

