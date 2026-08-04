**Example 1: demo**



Input: 

```
tccli es ModifyAutoScaleDiskInfo --cli-unfold-argument  \
    --InstanceId es-xxx \
    --AutoScaleDiskInfoList.0.NodeType hotData \
    --AutoScaleDiskInfoList.0.ScaleType 0 \
    --AutoScaleDiskInfoList.0.Threshold 80 \
    --AutoScaleDiskInfoList.0.Duration 60 \
    --AutoScaleDiskInfoList.0.PercentSize 20 \
    --AutoScaleDiskInfoList.0.FixSize 0 \
    --AutoScaleDiskInfoList.0.MaxSize 500 \
    --AutoScaleDiskInfoList.1.NodeType WarmData \
    --AutoScaleDiskInfoList.1.ScaleType 1 \
    --AutoScaleDiskInfoList.1.Threshold 0 \
    --AutoScaleDiskInfoList.1.Duration 90 \
    --AutoScaleDiskInfoList.1.PercentSize 0 \
    --AutoScaleDiskInfoList.1.FixSize 100 \
    --AutoScaleDiskInfoList.1.MaxSize 1000
```

Output: 
```
{
    "Response": {
        "Status": true,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

