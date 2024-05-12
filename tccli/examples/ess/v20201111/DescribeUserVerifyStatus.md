**Example 1: 通过二要素查询用户是否实名**

通过二要素查询用户是否实名

Input: 

```
tccli ess DescribeUserVerifyStatus --cli-unfold-argument  \
    --Operator.UserId abc \
    --Name abc \
    --IdCardNumber abc
```

Output: 
```
{
    "Response": {
        "VerifyStatus": true,
        "RequestId": "abc"
    }
}
```

