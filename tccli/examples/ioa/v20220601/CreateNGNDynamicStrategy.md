**Example 1: 示例**

创建动态访问策略

Input: 

```
tccli ioa CreateNGNDynamicStrategy --cli-unfold-argument  \
    --Name abc \
    --Description abc \
    --Status 0 \
    --Level 0 \
    --ActionResult abc \
    --Hint abc \
    --UserScope.UserIds 0 \
    --UserScope.GroupIds 0 \
    --UserScope.VirtualGroupIds 0 \
    --ResourceScope.ResourceIds 0 \
    --ResourceScope.ResourceGroupIds 0 \
    --TimeCondition.Type abc \
    --TimeCondition.TimeScope abc \
    --TimeCondition.DateScope abc \
    --TimeCondition.WeekDays 0 \
    --TimeCondition.Months 0 \
    --LocationCondition.Type abc \
    --LocationCondition.IPAreaIds 0 \
    --LocationCondition.LocationCodes abc \
    --PlatformCondition.Type abc \
    --PlatformCondition.Platforms abc \
    --AppProcessCondition.Type abc \
    --AppProcessCondition.AppIds 0 \
    --AppProcessCondition.AppCategoryIds 0 \
    --ComplianceCondition.Type abc \
    --ComplianceCondition.LevelScope abc \
    --UserRiskCondition.Type abc \
    --UserRiskCondition.LevelScope abc \
    --DeviceCondition.Type abc \
    --DeviceCondition.DeviceIds 0 \
    --DeviceCondition.DeviceVirtualGroupIds 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

