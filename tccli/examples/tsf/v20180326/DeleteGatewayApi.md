**Example 1: 批量删除API**



Input: 

```
tccli tsf DeleteGatewayApi --cli-unfold-argument  \
    --GroupId grp-5yk7oor1 \
    --ApiIdList api-d5970cd2 api-d5970cd3
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

