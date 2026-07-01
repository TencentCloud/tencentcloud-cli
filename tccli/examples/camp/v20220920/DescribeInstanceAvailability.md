**Example 1: 创建实例预测资源是否满足要求**



Input: 

```
tccli camp DescribeInstanceAvailability --cli-unfold-argument  \
    --ProjectID prj-xxxxxx \
    --ApplicationID app-xxxxxx \
    --EnvironmentName development \
    --Name qwe \
    --Components.0.Name qwe \
    --Components.0.Type deployment \
    --Components.0.Properties.Deployment {"kind":"Deployment","apiVersion":"apps/v1","metadata":{"name":"gpu","labels":{"k8s-app":"gpu"},"annotations":{"descheduler.alpha.kubernetes.io/pdb":"5"}},"spec":{"replicas":1,"template":{"metadata":{"annotations":{},"labels":{"k8s-app":"gpu"}},"spec":{"terminationGracePeriodSeconds":30,"containers":[{"name":"c","image":"c:c","env":[],"envForm":[],"resources":{"limits":{"cpu":"1","memory":"2Gi","tke.cloud.tencent.com/qgpu-core":10,"tke.cloud.tencent.com/qgpu-memory":1},"requests":{"cpu":"1","memory":"2Gi","tke.cloud.tencent.com/qgpu-core":10,"tke.cloud.tencent.com/qgpu-memory":1}}}],"imagePullSecrets":[{"name":"csighub-andrewren"}]}},"selector":{"matchLabels":{"k8s-app":"gpu"}}}} \
    --Components.0.Traits.0.Type replicas \
    --Components.0.Traits.0.Properties.Replicas.Replicas 2 \
    --Policies.0.Name gz \
    --Policies.0.Type placement \
    --Policies.0.Properties.Placement.Type dynamic \
    --Policies.0.Properties.Placement.Region ap-guangzhou \
    --Policies.0.Properties.Placement.Components qwe \
    --Policies.0.Properties.Placement.Zones.0.Zone * \
    --Policies.0.Properties.Placement.MinZones 2 \
    --Policies.0.Properties.Placement.Strategy Capacity
```

Output: 
```
{
    "Response": {
        "ResourceSatisfied": true,
        "Message": "",
        "HpaStatus": false,
        "ZoneAvailabilityCount": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-4",
                "Count": 27,
                "Cpu": 27,
                "Memory": 54,
                "GpuCore": 2.7,
                "GpuMemory": 27,
                "RequestCpu": 2,
                "RequestMemory": 4,
                "RequestGpuCore": 0.2,
                "RequestGpuMemory": 2,
                "MinRequestCpu": 0,
                "MinRequestMemory": 0,
                "MinRequestGpuCore": 0,
                "MinRequestGpuMemory": 0
            },
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-7",
                "Count": 0,
                "Cpu": 0,
                "Memory": 0,
                "GpuCore": 0,
                "GpuMemory": 0,
                "RequestCpu": 0,
                "RequestMemory": 0,
                "RequestGpuCore": 0,
                "RequestGpuMemory": 0,
                "MinRequestCpu": 0,
                "MinRequestMemory": 0,
                "MinRequestGpuCore": 0,
                "MinRequestGpuMemory": 0
            },
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-6",
                "Count": 0,
                "Cpu": 0,
                "Memory": 0,
                "GpuCore": 0,
                "GpuMemory": 0,
                "RequestCpu": 0,
                "RequestMemory": 0,
                "RequestGpuCore": 0,
                "RequestGpuMemory": 0,
                "MinRequestCpu": 0,
                "MinRequestMemory": 0,
                "MinRequestGpuCore": 0,
                "MinRequestGpuMemory": 0
            },
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "Count": 0,
                "Cpu": 0,
                "Memory": 0,
                "GpuCore": 0,
                "GpuMemory": 0,
                "RequestCpu": 0,
                "RequestMemory": 0,
                "RequestGpuCore": 0,
                "RequestGpuMemory": 0,
                "MinRequestCpu": 0,
                "MinRequestMemory": 0,
                "MinRequestGpuCore": 0,
                "MinRequestGpuMemory": 0
            }
        ],
        "RequestId": "8bf7756e-b882-4265-836a-c5d98bff8497"
    }
}
```

