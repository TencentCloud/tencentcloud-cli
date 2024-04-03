**Example 1: 绑定SaaS账号**



Input: 

```
tccli account AddAccountBindForSaaS --cli-unfold-argument  \
    --Platform cmp \
    --Account 122232
```

Output: 
```
{
    "Response": {
        "RequestId": "07635a8a-718d-4264-8edd-73b2dd606e78"
    }
}
```

**Example 2: 绑定登录账号**



Input: 

```
tccli account AddAccountBindForSaaS --cli-unfold-argument  \
    --Account 132****1234 \
    --Platform co**ng
```

Output: 
```
{
    "Response": {
        "RequestId": "748cff28-3afd-4a8d-9a80-d783729d9a1f"
    }
}
```

