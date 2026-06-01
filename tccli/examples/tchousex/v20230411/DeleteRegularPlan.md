**Example 1: 删除定时启停计划**



Input: 

```
tccli tchousex DeleteRegularPlan --cli-unfold-argument  \
    --RegularPlan.InstanceID abc \
    --RegularPlan.VirtualCluster abc \
    --RegularPlan.Component abc \
    --RegularPlan.StartTime abc \
    --RegularPlan.StopTime abc \
    --RegularPlan.Days abc \
    --RegularPlan.T1 abc \
    --RegularPlan.RoundType abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

