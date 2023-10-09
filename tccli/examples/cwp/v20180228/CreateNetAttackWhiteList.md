**Example 1: 创建网络攻击白名单**

创建网络攻击白名单

Input: 

```
tccli cwp CreateNetAttackWhiteList --cli-unfold-argument  \
    --Scope 1 \
    --SrcIp 127.0.0.1 \
    --DealOldEvents 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d42164cf-3e4e-49b8-ab55-adf942c609db"
    }
}
```

