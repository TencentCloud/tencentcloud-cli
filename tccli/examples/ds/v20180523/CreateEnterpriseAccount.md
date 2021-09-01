**Example 1: 创建企业帐号**

创建企业帐号

Input: 

```
tccli ds CreateEnterpriseAccount --cli-unfold-argument  \
    --Module AccountMng \
    --Operation CreateEnterpriseAccount \
    --Name test \
    --IdentType 8 \
    --IdentNo 140926197802256717 \
    --MobilePhone 18187654321 \
    --TransactorName test1 \
    --TransactorIdentType 0 \
    --TransactorIdentNo 140926197802256717 \
    --TransactorPhone 18287654321
```

Output: 
```
{
    "Response": {
        "AccountResId": "dcu-cw3uil4app",
        "RequestId": "0e72495a-2b48-4b5d-b425-38570fade1f8"
    }
}
```

