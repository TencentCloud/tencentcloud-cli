**Example 1: 查询实例的 CPU 弹性扩容策略**



Input: 

```
tccli cdb DescribeCPUExpandStrategyInfo --cli-unfold-argument  \
    --InstanceId cdb-sad1dsfa
```

Output: 
```
{
    "Response": {
        "Type": "auto",
        "ExpandCpu": 4,
        "AutoStrategy": {
            "ExpandThreshold": 0,
            "ShrinkThreshold": 0,
            "ExpandPeriod": 0,
            "ShrinkPeriod": 0
        },
        "RequestId": "sasd8asf-f78asd-fas8-dga9-gdfadf1234"
    }
}
```

