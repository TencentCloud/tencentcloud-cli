**Example 1: 查询预留券使用率**

预留券使用率

Input: 

```
tccli tke DescribeReservedInstanceUtilizationRate --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PodNum": 1,
        "PodRate": 0,
        "UtilizationRateSet": [
            {
                "Rate": 0,
                "Num": 1,
                "PodNum": 1,
                "CPU": 1,
                "Memory": 2,
                "Type": "common",
                "GpuNum": "",
                "Zone": "",
                "ClusterId": "",
                "NodeName": ""
            }
        ],
        "RequestId": "0be873cf-014f-408b-8527-03c25c32725b"
    }
}
```

