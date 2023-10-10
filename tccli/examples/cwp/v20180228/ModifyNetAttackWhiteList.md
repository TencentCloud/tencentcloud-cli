**Example 1: 编辑网络攻击白名单**

编辑网络攻击白名单

Input: 

```
tccli cwp ModifyNetAttackWhiteList --cli-unfold-argument  \
    --QuuidList 05f0bcab-726c-4ea4-8109-bcd03d5598f7 \
    --Scope 0 \
    --SrcIp 1.2.3.5 1.1.1.2-1.1.1.4 1.2.3.0/24 \
    --DealOldEvents 0 \
    --Description 123 \
    --Id 10001
```

Output: 
```
{
    "Response": {
        "RequestId": "1a07706f-368e-49e5-8967-594826f43d0d"
    }
}
```

