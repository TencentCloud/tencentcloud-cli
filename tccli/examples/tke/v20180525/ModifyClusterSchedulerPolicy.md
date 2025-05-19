**Example 1: 修改集群调度策略**

修改集群调度策略

Input: 

```
tccli tke ModifyClusterSchedulerPolicy --cli-unfold-argument  \
    --ClusterId cls-kasybnzk \
    --Priorities.0.Name EvenPodsSpreadPriority \
    --Priorities.0.Weight 2 \
    --Priorities.1.Name TaintTolerationPriority \
    --Priorities.1.Weight 1 \
    --Priorities.2.Name InterPodAffinityPriority \
    --Priorities.2.Weight 1 \
    --Priorities.3.Name LeastRequestedPriority \
    --Priorities.3.Weight 2 \
    --Priorities.4.Name NodeAffinityPriority \
    --Priorities.4.Weight 1 \
    --Priorities.5.Name NodePreferAvoidPodsPriority \
    --Priorities.5.Weight 10000 \
    --Priorities.6.Name BalancedResourceAllocation \
    --Priorities.6.Weight 1 \
    --Priorities.7.Name SelectorSpreadPriority \
    --Priorities.7.Weight 1 \
    --Priorities.8.Name ImageLocalityPriority \
    --Priorities.8.Weight 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c39624e5-9536-4cd0-a3b2-8830cdfef2a1"
    }
}
```

