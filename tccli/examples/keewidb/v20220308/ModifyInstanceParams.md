**Example 1: 示例1**



Input: 

```
tccli keewidb ModifyInstanceParams --cli-unfold-argument  \
    --InstanceId kee-9clk**** \
    --InstanceParams.0.Key auto-failback \
    --InstanceParams.0.Value no
```

Output: 
```
{
    "Response": {
        "Changed": false,
        "RequestId": "8acefa7e-22c9-4332-ab9c-175681e95a31",
        "TaskId": 1634784474
    }
}
```

