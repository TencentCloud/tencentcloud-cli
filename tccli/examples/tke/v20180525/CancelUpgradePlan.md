**Example 1: 取消集群升级计划**

取消一个集群组件的升级计划

Input: 

```
tccli tke CancelUpgradePlan --cli-unfold-argument  \
    --ClusterID cls-3n90hta2 \
    --PlanID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26"
    }
}
```

