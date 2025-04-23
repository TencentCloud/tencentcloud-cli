**Example 1: 获取cpu平均 使用率**



Input: 

```
tccli dlc DescribeClusterMonitorInfos --cli-unfold-argument  \
    --DataEngineId dataengine-9omoklhv
```

Output: 
```
{
    "Response": {
        "Info": "{\"cluster_cpu_usage_average\":[8.65515625]}",
        "RequestId": "87bb46a9-1ff4-455e-92b5-fc4dd86bf0c2"
    }
}
```

