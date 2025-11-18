**Example 1: 查询可降配次数**



Input: 

```
tccli cvm DescribeInstancesOperationLimit --cli-unfold-argument  \
    --InstanceIds ins-r7ov05ke \
    --Operation INSTANCE_DEGRADE
```

Output: 
```
{
    "Response": {
        "InstanceOperationLimitSet": [
            {
                "CurrentCount": 0,
                "InstanceId": "ins-r7ov05ke",
                "LimitCount": 5,
                "Operation": "INSTANCE_DEGRADE"
            }
        ],
        "RequestId": "ce7aeaa3-37c9-48e2-abbf-7c1264cf5e9c"
    }
}
```

