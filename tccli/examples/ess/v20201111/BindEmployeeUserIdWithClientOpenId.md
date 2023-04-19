**Example 1: 示例1**

传入OpenId

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.Channel INTEGRATE \
    --Operator.OpenId 12345 \
    --UserId ************ \
    --OpenId ***********
```

Output: 
```
{
    "Response": {
        "RequestId": "s1665218505798774974",
        "Status": 1
    }
}
```

**Example 2: 示例2**

传入UserId

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.UserId ************** \
    --UserId ************ \
    --OpenId ***********
```

Output: 
```
{
    "Response": {
        "RequestId": "s1665218590874024539",
        "Status": 1
    }
}
```

