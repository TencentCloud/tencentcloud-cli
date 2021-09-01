**Example 1: 新增个人帐号**

新增个人帐号

Input: 

```
tccli ds CreatePersonalAccount --cli-unfold-argument  \
    --Module AccountMng \
    --Operation CreatePersonalAccount \
    --Name test \
    --IdentType 0 \
    --IdentNo 140926197802256717 \
    --MobilePhone 18187654321
```

Output: 
```
{
    "Response": {
        "AccountResId": "dcu-9mxcxe2mmt",
        "RequestId": "ca67c21d-28c8-4d20-ba3e-b3f4bc1813b4"
    }
}
```

