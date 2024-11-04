**Example 1: 修改SCIM密钥状态**

修改SCIM密钥状态

Input: 

```
tccli organization UpdateSCIMCredentialStatus --cli-unfold-argument  \
    --ZoneId z-vft38p2hq8tq \
    --CredentialId scimcred-un1tgbnt0s9j \
    --NewStatus Disabled
```

Output: 
```
{
    "Response": {
        "RequestId": "d0b5fffc-c7b9-4513-a080-8dfcf72c6e56"
    }
}
```

