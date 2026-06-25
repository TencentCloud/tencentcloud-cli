**Example 1: 重置用户密码**



Input: 

```
tccli tdmysql ResetUserPassword --cli-unfold-argument  \
    --UserName test_user \
    --InstanceId tdsql3-d8fffc3c \
    --Host % \
    --Password dasdfadasdf231!@
```

Output: 
```
{
    "Response": {
        "RequestId": "a93d2900-ef72-11eb-ab93-0716f253da76"
    }
}
```

**Example 2: 重置用户加密密码**

使用加密密码重置用户密码

Input: 

```
tccli tdmysql ResetUserPassword --cli-unfold-argument  \
    --UserName test1234567 \
    --InstanceId tdsql3-f44c7c8e \
    --Host % \
    --EncryptedPassword lNepasen9UqXCGYFXc3kkT2GIa5Byc+8CcCOCkTxxTZ/Dow03USfrJrnTLB9cclK6k3RWruGAnP7CbogfauT2otyiIepAEfGK5fHgOZwZCfgrM3J6/K2nxTdYaYjtQP6cyMYbW+07/EdKpUSOpv+6MGw3nPDPrJFDNOvt8EjEbJ9+fU/zC+O4CNX7HdHNeWUtlMRtTEIeqXInjYb5M32aB01SrIEWSel6K2SMpjjzXsKqSVZl/nrHkWsXTd5Xn8ysuV/2Eu1dipXVbhR8lWQ1y57qopPIuz0v2ARODgVTPyY550g/hl3Tz7ScJxynJEL4AajBy7i8po0WA5Ctg1Eiw==
```

Output: 
```
{
    "Response": {
        "RequestId": "15636f30-1e3f-4d8b-887c-c1eae1a1cc78"
    }
}
```

