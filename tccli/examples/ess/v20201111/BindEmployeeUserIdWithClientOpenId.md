**Example 1: 示例1**



Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.UserId  \
    --Operator.Channel CLOUD_API \
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



Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.UserId ************** \
    --Operator.Channel  \
    --Operator.OpenId  \
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

