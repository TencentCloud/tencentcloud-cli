**Example 1: 更新凭据描述信息**



Input: 

```
tccli ssm UpdateDescription --cli-unfold-argument  \
    --SecretName test \
    --Description 'new desc'
```

Output: 
```
{
    "Response": {
        "RequestId": "dfa4908b-a586-4d44-8f76-3fad156c1be2",
        "SecretName": "test"
    }
}
```

