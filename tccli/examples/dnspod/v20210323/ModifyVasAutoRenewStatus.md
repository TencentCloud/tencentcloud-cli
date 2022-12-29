**Example 1: 增值服务关闭自动续费**

 

Input: 

```
tccli dnspod ModifyVasAutoRenewStatus --cli-unfold-argument  \
    --ResourceId a0bed80e \
    --Status disable
```

Output: 
```
{
    "Response": {
        "RequestId": "896a1b04-814d-49d1-b404-42cc8d5b67f0"
    }
}
```

**Example 2: 增值服务开启自动续费**

 

Input: 

```
tccli dnspod ModifyVasAutoRenewStatus --cli-unfold-argument  \
    --ResourceId a0bed80e \
    --Status enable
```

Output: 
```
{
    "Response": {
        "RequestId": "896a1b04-814d-49d1-b404-42cc8d5b67f0"
    }
}
```

