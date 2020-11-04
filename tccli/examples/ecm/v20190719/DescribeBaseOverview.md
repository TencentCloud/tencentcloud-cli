**Example 1: 展示概览页基础统计数据**

展示概览页基础统计数据

Input: 

```
tccli ecm DescribeBaseOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "62914bef-f8fb-44a5-83a8-df8fe1324f3c",
        "InstanceNum": 5,
        "RunningNum": 4,
        "IsolationNum": 0,
        "ModuleNum": 12,
        "NodeNum": 2,
        "VcpuNum": 12,
        "MemoryNum": 24,
        "StorageNum": 250,
        "NetworkNum": 0,
        "ExpiredNum": 0,
        "WillExpireNum": 0
    }
}
```

