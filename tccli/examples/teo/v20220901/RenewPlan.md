**Example 1: 续费套餐三个月**

续费套餐 edgeone-2unuvzjmmn2q 时长 3 个月，且不自动使用代金券。

Input: 

```
tccli teo RenewPlan --cli-unfold-argument  \
    --PlanId edgeone-2unuvzjmmn2q \
    --Period 3 \
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

