**Example 1: 将预付费套餐升级至标准版**

将预付费套餐 edgeone-2unuvzjmmn2q 升级至标准版，且不使用代金券。

Input: 

```
tccli teo UpgradePlan --cli-unfold-argument  \
    --PlanId edgeone-2unuvzjmmn2q \
    --PlanType standard \
    --AutoUseVoucher false
```

Output: 
```
{
    "Response": {
        "DealName": "20240312347001004723731",
        "RequestId": "6a617014-efc9-45c6-ba9d-c87d70472461"
    }
}
```

