**Example 1: 取消计划**



Input: 

```
tccli cynosdb CancelClusterServerlessScalePlan --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xdbsbsgg \
    --PlanId 12321
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

