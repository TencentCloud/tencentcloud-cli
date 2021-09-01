**Example 1: 查询可降配次数**



Input: 

```
tccli cvm DescribeInstancesOperationLimit --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy \
    --Operation INSTANCE_DEGRADE
```

Output: 
```
{
    "Response": {
        "InstanceOperationLimitSet": [
            {
                "Operation": "INSTANCE_DEGRADE",
                "InstanceId": "ins-r8hr2upy",
                "CurrentCount": 0,
                "LimitCount": 5
            }
        ],
        "RequestId": "951caf78-580f-42f6-8b83-a902d051d672"
    }
}
```

