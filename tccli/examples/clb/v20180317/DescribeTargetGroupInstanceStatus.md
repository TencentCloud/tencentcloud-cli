**Example 1: 批量查询gwlb目标组后端服务状态**

批量查询gwlb目标组后端服务状态

Input: 

```
tccli clb DescribeTargetGroupInstanceStatus --cli-unfold-argument  \
    --TargetGroupId lbtg-3j3**** \
    --TargetGroupInstanceIps 10.0.1.13 10.0.1.5
```

Output: 
```
{
    "Response": {
        "RequestId": "b3ba6587-1a1c-47eb-ac8b-0424bf3fdc86",
        "TargetGroupInstanceSet": [
            {
                "InstanceIp": "10.0.1.13",
                "Status": "on"
            },
            {
                "InstanceIp": "10.0.1.5",
                "Status": "on"
            }
        ]
    }
}
```

