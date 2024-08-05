**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeUserDetail --cli-unfold-argument  \
    --UserId abc \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "UserId": "abc",
            "UserAccount": "abc",
            "AccountType": 0,
            "UserName": "abc"
        },
        "RequestId": "abc"
    }
}
```

