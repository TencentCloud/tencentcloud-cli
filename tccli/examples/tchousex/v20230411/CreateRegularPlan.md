**Example 1: 定时启停示例**



Input: 

```
tccli tchousex CreateRegularPlan --cli-unfold-argument  \
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

