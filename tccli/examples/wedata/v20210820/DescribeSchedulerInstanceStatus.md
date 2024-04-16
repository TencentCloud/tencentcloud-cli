**Example 1: 实例状态分布示例**

实例状态分布

Input: 

```
tccli wedata DescribeSchedulerInstanceStatus --cli-unfold-argument  \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CountTag": 0,
                "DependencyNum": 0,
                "FailedNum": 5540,
                "RunningNum": 0,
                "StoppingNum": 0,
                "SucceedNum": 1425,
                "TotalNum": 6965,
                "WaitEventNum": "0",
                "WaitRunningNum": 0
            }
        ],
        "RequestId": "851a90c2-5c3e-4931-818d-66155133784b"
    }
}
```

