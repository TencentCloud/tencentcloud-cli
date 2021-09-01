**Example 1: 更改API**



Input: 

```
tccli tsf UpdateGatewayApi --cli-unfold-argument  \
    --ApiId api-5yk7oor1 \
    --Path /user/find \
    --Method POST \
    --PathMapping /user/find
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a",
        "Result": true
    }
}
```

