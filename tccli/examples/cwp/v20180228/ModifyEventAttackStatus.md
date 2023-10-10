**Example 1: 修改网络攻击事件状态**

修改网络攻击事件状态

Input: 

```
tccli cwp ModifyEventAttackStatus --cli-unfold-argument  \
    --Ids 1 \
    --All False \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4a45604e-1d2b-423c-9b45-31d1633dc8d2"
    }
}
```

