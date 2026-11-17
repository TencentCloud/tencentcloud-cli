**Example 1: 查询用户级访问凭证**



Input: 

```
tccli workbuddyenterprise DescribeUserAccessToken --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessToken": "eyJhbGciOiJIUzI1NiJ9.signature",
        "TokenType": "Bearer",
        "ExpiresIn": 3600,
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

