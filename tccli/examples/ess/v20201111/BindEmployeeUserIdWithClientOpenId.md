**Example 1: 示例1**

传入OpenId

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.Channel INTEGRATE \
    --Operator.OpenId 12345 \
    --UserId *yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --OpenId open_user1
```

Output: 
```
{
    "Response": {
        "RequestId": "s166521xxxx8774974",
        "Status": 1
    }
}
```

**Example 2: 示例2**

传入UserId

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQxx2u1 \
    --UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --OpenId open_user2
```

Output: 
```
{
    "Response": {
        "RequestId": "s1665xxxxx74024539",
        "Status": 1
    }
}
```

