**Example 1: 查询用户零预付模式**

根据uin查询用户零预付模式开关

Input: 

```
tccli billing DescribeSalesPolicy --cli-unfold-argument  \
    --ProductCode p_tqdcs \
    --SubProductCode sp_tqdcs
```

Output: 
```
{
    "Response": {
        "NoUpfrontRIs": "recommended",
        "RequestId": "c49fd5c2-1f59-4ee5-97f0-d1c158dc5691"
    }
}
```

