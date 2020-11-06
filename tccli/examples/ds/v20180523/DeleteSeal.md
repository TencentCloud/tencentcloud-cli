**Example 1: 删除签章**

删除签章

Input: 

```
tccli ds DeleteSeal --cli-unfold-argument  \
    --Module SealMng \
    --Operation DeleteSeal \
    --AccountResId dcu-c33udl4apd \
    --SealResId dcs-hr6tc1vtir
```

Output: 
```
{
    "Response": {
        "RequestId": "8a01c0a9-d7e5-42b4-8147-c22b9a6e31f8",
        "SealResId": "dcs-hr6tc1vtir"
    }
}
```

