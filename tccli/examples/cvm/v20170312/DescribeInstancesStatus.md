**Example 1: 查看实例状态列表**

本示例用于查看实例状态列表中的两个实例。

Input: 

```
tccli cvm DescribeInstancesStatus --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceStatusSet": [
            {
                "InstanceId": "ins-r8hr2upy",
                "InstanceState": "RUNNING"
            },
            {
                "InstanceId": "ins-5d8a23rs",
                "InstanceState": "STOPPED"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

