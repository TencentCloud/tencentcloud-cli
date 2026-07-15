**Example 1: 查询全量撤销企业合同任务结果**

查询全量撤销企业合同任务结果

Input: 

```
tccli ess DescribeCancelFlowsTask --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --TaskId yD3POUUckpzz6onbUy8Im5DBfEstv2zM \
    --CancelType 1
```

Output: 
```
{
    "Response": {
        "FailureFlows": [],
        "SuccessFlowIds": [
            "yD3PCUUckpzv5at9U1UxZEpOywg0E9oG"
        ],
        "TaskId": "yD3POUUckpzz6onbUy8Im5DBfEstv2zM",
        "TaskStatus": "END",
        "RequestId": "b3c22211-aec1-4948-8676-28c1f1d33f87"
    }
}
```

**Example 2: 查询批量撤销任务结果**

通过TaskId查询批量撤销任务结果

Input: 

```
tccli ess DescribeCancelFlowsTask --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --TaskId yDCVWUUckpwkjgiuUWGW8cRAzd93BVQb
```

Output: 
```
{
    "Response": {
        "FailureFlows": [
            {
                "FlowId": "yDCNGUUckpvjdelbUuyImI9pY8I5Mep1",
                "Reason": "合同当前状态不支持撤销"
            },
            {
                "FlowId": "yDCV4UUckpwr0wq7UENkSSawLpt5Fz6C",
                "Reason": "合同当前状态不支持撤销"
            },
            {
                "FlowId": "yDw9jUUgyg54g2mdUxawbT61HrwMQ2gF",
                "Reason": "合同信息不存在或非本企业发起的合同"
            }
        ],
        "RequestId": "8698cab8-5947-49e6-8681-ce2080b70e73",
        "SuccessFlowIds": [
            "yDCN0UUckpvhnc6uUuyImI98ydIEe6bX"
        ],
        "TaskId": "yDCVWUUckpwkjgiuUWGW9cRAzd93BVQa",
        "TaskStatus": "END"
    }
}
```

