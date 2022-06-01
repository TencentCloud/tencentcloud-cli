**Example 1: 修改默认证书状态**



Input: 

```
tccli teo ModifyDefaultCertificate --cli-unfold-argument  \
    --ZoneId zone-xxxx \
    --CertId EO-xxxx \
    --Status deploy
```

Output: 
```
{
    "Response": {
        "RequestId": "2346602a-0bbf-409b-922c-ae3071c27594"
    }
}
```

