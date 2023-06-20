**Example 1: SAML 断言申请角色临时访问凭证**

SAML 断言申请角色临时访问凭证

Input: 

```
tccli sts AssumeRoleWithSAML --cli-unfold-argument  \
    --RoleArn qcs::cam::uin/798950673:roleName/OneLogin-Role \
    --PrincipalArn qcs::cam::uin/798950673:saml-provider/OneLogin \
    --SAMLAssertion c2FtbCBhc3NlcnRpb24= \
    --RoleSessionName test
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "1siMD***5ue",
            "TmpSecretId": "AKID****H58",
            "TmpSecretKey": "q95K****yoh"
        },
        "ExpiredTime": 1543914376,
        "Expiration": "2018-12-04T09:06:16Z",
        "RequestId": "4daec797-9cd2-4f09-9e7a-7d4c43b2a74c"
    }
}
```

