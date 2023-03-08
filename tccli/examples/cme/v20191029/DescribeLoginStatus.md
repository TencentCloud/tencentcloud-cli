**Example 1: 查询用户登录态**

 

Input: 

```
tccli cme DescribeLoginStatus --cli-unfold-argument  \
    --Platform test \
    --UserIds user_id_5285890811433511063 user_id_5285890811433511064
```

Output: 
```
{
    "Response": {
        "LoginStatusInfoSet": [
            {
                "UserId": "user_id_5285890811433511063",
                "Status": "Online"
            },
            {
                "UserId": "user_id_5285890811433511064",
                "Status": "Offline"
            }
        ],
        "RequestId": "requestId"
    }
}
```

