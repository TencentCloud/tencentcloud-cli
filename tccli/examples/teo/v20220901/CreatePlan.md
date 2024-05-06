**Example 1: 创建个人版计费套餐**

创建个人版计费套餐，套餐时长 1 个月，且设置不自动续费。

Input: 

```
tccli teo CreatePlan --cli-unfold-argument  \
    --PlanType personal \
    --PrepaidPlanParam.Period 1 \
    --PrepaidPlanParam.RenewFlag off \
    --AutoUseVoucher false
```

Output: 
```
{
    "Response": {
        "RequestId": "6a617014-efc9-45c6-ba9d-c87d70472461",
        "PlanId": "edgeone-2unuvzjmmn2q",
        "DealName": "20240312347001004723731"
    }
}
```

**Example 2: 创建企业版套餐**

创建企业版套餐。

Input: 

```
tccli teo CreatePlan --cli-unfold-argument  \
    --PlanType enterprise
```

Output: 
```
{
    "Response": {
        "RequestId": "6a617014-efc9-45c6-ba9d-c87d70472461",
        "PlanId": "edgeone-2unuvzjmmn2q",
        "DealName": "20240312347001004723731"
    }
}
```

