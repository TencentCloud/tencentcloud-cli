**Example 1: 示例**



Input: 

```
tccli cdwch ScaleUpInstance --cli-unfold-argument  \
    --InstanceId cdwch-nzb9s4zz \
    --Type DATA \
    --SpecName SCH1 \
    --ScaleUpEnableRolling False
```

Output: 
```
{
    "Response": {
        "InstanceId": "cdwch-xxxxxxxx",
        "FlowId": "001",
        "RequestId": "20a71202-27c4-4120-80c4-fb1a8e15dxxx",
        "ErrorMsg": "InvalidParameter"
    }
}
```

