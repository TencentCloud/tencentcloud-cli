**Example 1: 创建全球加速实例**



Input: 

```
tccli ga2 CreateGlobalAccelerator --cli-unfold-argument  \
    --Name garendu-test-05 \
    --InstanceChargeType POSTPAID \
    --Description garendu-test-05
```

Output: 
```
{
    "Response": {
        "GlobalAcceleratorId": "ga-fkp17vr8",
        "RequestId": "02eb3789-7d73-4b09-94de-c2750cfa1b63",
        "TaskId": "dfcfbd3b-fe76-434b-8ce3-d6c11a5d4226"
    }
}
```

