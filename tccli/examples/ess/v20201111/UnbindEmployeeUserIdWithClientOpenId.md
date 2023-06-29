**Example 1: 示例1**

传入OpenId

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.Channel INTEGRATE \
    --Operator.OpenId 12345 \
    --UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --OpenId open_user1
```

Output: 
```
{
    "Response": {
        "RequestId": "s16653xxxxx98336866",
        "Status": 1
    }
}
```

**Example 2: 示例2**

传入userId

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId *yDwgKUUcXXXXXXXXXXXXXXXXXXQZxxs32 \
    --UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --OpenId open_user1
```

Output: 
```
{
    "Response": {
        "RequestId": "s16652185xxx032958",
        "Status": 1
    }
}
```

