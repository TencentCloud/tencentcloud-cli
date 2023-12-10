**Example 1: 示例1**

更改多az实例可用区(时间窗口切换)

Input: 

```
tccli redis ModifyInstanceAvailabilityZones --cli-unfold-argument  \
    --InstanceId crs-rrhr1lm6 \
    --SwitchOption 1 \
    --NodeSet.0.NodeId 339472 \
    --NodeSet.0.NodeType 0 \
    --NodeSet.0.ZoneId 100004 \
    --NodeSet.1.NodeId 339473 \
    --NodeSet.1.NodeType 1 \
    --NodeSet.1.ZoneId 100003 \
    --NodeSet.2.NodeId 339549 \
    --NodeSet.2.NodeType 1 \
    --NodeSet.2.ZoneId 100003
```

Output: 
```
{
    "Response": {
        "RequestId": "27c0d6e8-9894-42e0-a03b-814a204437ba",
        "TaskId": 2031290200
    }
}
```

