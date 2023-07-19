**Example 1: 示例1**

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
                "CountTag": 1,
                "TotalNum": 1,
                "RunningNum": 1,
                "WaitRunningNum": 1,
                "DependencyNum": 1,
                "WaitEventNum": "abc",
                "StoppingNum": 1,
                "SucceedNum": 1,
                "FailedNum": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

