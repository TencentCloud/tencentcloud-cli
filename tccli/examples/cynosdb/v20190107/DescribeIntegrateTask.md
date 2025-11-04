**Example 1: 查询集成任务**

Describe Integrate Task

Input: 

```
tccli cynosdb DescribeIntegrateTask --cli-unfold-argument  \
    --DealNames 20250922456021575003931
```

Output: 
```
{
    "Response": {
        "CurrentProgress": "5/5",
        "CurrentStep": "FinishTask",
        "RequestId": "de351c1d-72fa-477b-997a-8ae045f90da2",
        "TaskStatus": "success"
    }
}
```

