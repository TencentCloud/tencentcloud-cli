**Example 1: 通过二要素查询用户是否实名**

通过二要素查询用户是否实名

Input: 

```
tccli ess DescribeUserVerifyStatus --cli-unfold-argument  \
    --Operator.UserId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP \
    --Name 典子谦 \
    --IdCardNumber 620000198802020000 \
    --IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "VerifyStatus": true,
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 "
    }
}
```

