**Example 1: 查询YARN资源调度的全局配置**



Input: 

```
tccli emr DescribeGlobalConfig --cli-unfold-argument  \
    --InstanceId emr-xxx
```

Output: 
```
{
    "Response": {
        "ActiveScheduler": "fair",
        "CapacityGlobalConfig": {
            "DefaultSettings": [
                {
                    "Desc": "保证任务本地化执行，可以延迟调度的次数，如果值为 -1，将禁用延迟调度。",
                    "Key": "yarn.scheduler.capacity.node-locality-delay",
                    "Name": "node-locality-delay",
                    "Prompt": "请输入-1和0、正整数",
                    "Value": null
                },
                {
                    "Desc": "是否允许在一次NodeManager心跳中分配多个容器。默认为true。需重启ResourceManager。",
                    "Key": "yarn.scheduler.capacity.per-node-heartbeat.multiple-assignments-enabled",
                    "Name": "multiple-assignments-enabled",
                    "Prompt": "请输入true或者false",
                    "Value": null
                },
                {
                    "Desc": "如果multiple-assignments-enabled为true，在一次NodeManager心跳中可以分配的最大容器数量。需重启ResourceManager。",
                    "Key": "yarn.scheduler.capacity.per-node-heartbeat.maximum-container-assignments",
                    "Name": "maximum-container-assignments",
                    "Prompt": "请输入-1和正整数",
                    "Value": null
                },
                {
                    "Desc": "用于比较调度程序中的资源的ResourceCalculator实现。默认的org.apache.hadoop.yarn.util.resource.DefaultResourceCalculator只使用内存，而org.apache.hadoop.yarn.util.resource.DominantResourceCalculator使用多维资源，如内存，CPU等。需重启ResourceManager。",
                    "Key": "yarn.scheduler.capacity.resource-calculator",
                    "Name": "resource-calculator",
                    "Prompt": "输入请参考描述信息",
                    "Value": null
                }
            ],
            "EnableLabel": false,
            "LabelDir": null,
            "QueueMappingOverride": null
        },
        "EnableResourceSchedule": true,
        "FairGlobalConfig": {
            "UserMaxAppsDefault": null
        },
        "RequestId": "37bd53ed-7516-4a36-988e-e4afeb731df1",
        "Scheduler": "fair"
    }
}
```

