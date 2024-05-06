**Example 1: 为套餐增购站点数配额**

为套餐 edgeone-2unuvzjmmn2q 增购 10 个站点数配额。

Input: 

```
tccli teo IncreasePlanQuota --cli-unfold-argument  \
    --PlanId edgeone-2unuvzjmmn2q \
    --QuotaType site \
    --QuotaNumber 10
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

**Example 2: 为套餐增购自定义规则配额**

为套餐 edgeone-2unuvzjmmn2q 增购 10 个 Web 防护 - 自定义规则 - 精准匹配策略的规则配额。

Input: 

```
tccli teo IncreasePlanQuota --cli-unfold-argument  \
    --PlanId edgeone-2unuvzjmmn2q \
    --QuotaType precise_access_control_rule \
    --QuotaNumber 10
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

