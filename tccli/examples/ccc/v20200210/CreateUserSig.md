**Example 1: 生成用户数据签名**



Input: 

```
tccli ccc CreateUserSig --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --Uid staff1@xxx.com \
    --ClientData abc \
    --ExpiredTime 86400
```

Output: 
```
{
    "Response": {
        "RequestId": "48edd236-7ef1-45af-9e12-fc376ba355bf",
        "UserSig": "eJw0jkFPwjAYQP-Ld9Wwfm2HtokHswhK9IBMBtw22uEHbpa1JRrjfzfZ5vW95OX9QP68mtgvR50FrYRSQonrHpKxbaCabAcaEFGmMAhvTqVzZECjZIxPJUc5GjqAho1fJMlpnlfb9iYJx2WZZ*YqnLO1m9Wrh-uXeD48ZR9vkYrl3ZgM1FjQOOXyNkXJ2UCjt10Va9CwLRbH3Xzd7Pi7K5vgqyK97B9n33vxiqY10m4*-1OX-pdPGPz*BQAA--9b7kId"
    }
}
```

