**Example 1: 示例1**

传入OpenId

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
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
        "RequestId": "s1665384640598336866",
        "Status": 1
    }
}
```

**Example 2: 示例2**

传入userId

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.UserId ************** \
    --UserId ************ \
    --OpenId ***********
```

Output: 
```
{
    "Response": {
        "RequestId": "s1665218558695032958",
        "Status": 1
    }
}
```

