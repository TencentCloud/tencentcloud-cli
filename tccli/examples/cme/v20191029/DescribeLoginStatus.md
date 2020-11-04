**Example 1: 查询用户登录态**



Input: 

```
tccli cme DescribeLoginStatus --cli-unfold-argument  \
    --Platform test\
    --UserIds 111
```

Output: 
```
{
    "Response": {
        "LoginStatusInfoSet": [],
        "RequestId": "requestId"
    }
}
```

