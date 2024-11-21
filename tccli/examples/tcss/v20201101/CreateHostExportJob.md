**Example 1: 创建主机列表导出任务**



Input: 

```
tccli tcss CreateHostExportJob --cli-unfold-argument  \
    --ExportField HostName HostIP PublicIp Group InstanceID MachineType Status DockerVersion ContainerdVersion DockerFileSystemDriver ImageCnt ContainerCnt
```

Output: 
```
{
    "Response": {
        "JobId": "73805b97-0e40-4249-8fe5-f1e38de1c28a",
        "RequestId": "78382c9e-92c7-42bb-8a2a-04d406903d94"
    }
}
```

