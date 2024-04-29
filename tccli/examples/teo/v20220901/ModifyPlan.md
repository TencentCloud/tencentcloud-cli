**Example 1: 修改预付费套餐自动续费标签**

开启预付费套餐 edgeone-2unuvzjmmn2q 的自动续费功能。

Input: 

```
tccli teo ModifyPlan --cli-unfold-argument  \
    --PlanId edgeone-2unuvzjmmn2q \
    --RenewFlag.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "6a617014-efc9-45c6-ba9d-c87d70472461"
    }
}
```

