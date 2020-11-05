**Example 1: Requesting for the temporary credentials for a role that has been authenticated via a SAML assertion**



Input: 

```
tccli sts AssumeRoleWithSAML --cli-unfold-argument  \
    --PrincipalArn qcs::cam::uin/798950673:saml-provider/OneLogin\
    --RoleArn qcs::cam::uin/798950673:roleName/OneLogin-Role\
    --RoleSessionName test\
    --SAMLAssertion c2FtbCBhc3NlcnRpb24
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "1siMD5r0tPAq9xpRlnzj4pjI8daS4MIW4dcd2a6a1ad76f09a0069002923def8aFw7tUMd2nH-yMZE5816oW7_Y-0JwI_ReMlkz-ajVxc_6MrXEYRtRShjDg5-L4Dq0ceupsIfdokiZG9EkfzO6Vt11iW0jLlPMT1pRFue",
            "TmpSecretId": "AKID65zyIP0mpXtaIFqt2SlWIQVMn1umNH58",
            "TmpSecretKey": "q95K84wrzuEGocfy39zg52boxvp71yoh"
        },
        "ExpiredTime": 1543914376,
        "Expiration": "2018-12-04T09:06:16Z",
        "RequestId": "4daec797-9cd2-4f09-9e7a-7d4c43b2a74c"
    }
}
```

