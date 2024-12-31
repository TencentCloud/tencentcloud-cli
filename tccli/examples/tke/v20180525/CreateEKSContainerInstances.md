**Example 1: 创建容器实例**

创建容器实例

Input: 

```
tccli tke CreateEKSContainerInstances --cli-unfold-argument  \
    --AutoCreateEipAttribute.InternetMaxBandwidthOut 1 \
    --AutoCreateEipAttribute.DeletePolicy Immediate \
    --AutoCreateEipAttribute.InternetServiceProvider BGP \
    --CamRoleName TkeRole \
    --VpcId vpc-12345678 \
    --DnsConfig.Nameservers server \
    --DnsConfig.Searches  \
    --DnsConfig.Options.0.Name  \
    --DnsConfig.Options.0.Value  \
    --Replicas 1 \
    --ImageRegistryCredentials.0.Username devops \
    --ImageRegistryCredentials.0.Password  \
    --ImageRegistryCredentials.0.Name ta-habor-registry-0 \
    --ImageRegistryCredentials.0.Server docker-ta.thinkingdata.cn \
    --EksCiVolume.CbsVolumes.0.CbsDiskId disk-45b3agyu \
    --EksCiVolume.CbsVolumes.0.Name disk-45b3agyu \
    --EksCiVolume.NfsVolumes.0.Path /5g326fcf/localfolder \
    --EksCiVolume.NfsVolumes.0.ReadOnly True \
    --EksCiVolume.NfsVolumes.0.Name vol \
    --EksCiVolume.NfsVolumes.0.Server 9.19.101.170 \
    --GpuCount 1 \
    --ExistedEipIds eip-12345678 \
    --AutoCreateEip True \
    --RestartPolicy Always \
    --Cpu 1.0 \
    --Memory 2.0 \
    --SubnetId subnet-12345678 \
    --CpuType amd,intel \
    --SecurityGroupIds sg-12345678 \
    --Containers.0.Commands sleep \
    --Containers.0.Name nginx \
    --Containers.0.GpuLimit 1 \
    --Containers.0.WorkingDir /var \
    --Containers.0.Image nginx:latest \
    --Containers.0.Args 10000 \
    --Containers.0.VolumeMounts.0.MountPropagation  \
    --Containers.0.VolumeMounts.0.ReadOnly True \
    --Containers.0.VolumeMounts.0.MountPath /images/mnt \
    --Containers.0.VolumeMounts.0.SubPath /images/mnt \
    --Containers.0.VolumeMounts.0.Name disk-45b3agyi \
    --Containers.0.RestartCount 1 \
    --Containers.0.EnvironmentVars.0.Name EKS_LOGS_OUTPUT_TYPE \
    --Containers.0.EnvironmentVars.0.Value cls \
    --Containers.0.Memory 0.0 \
    --Containers.0.Cpu 0.0 \
    --EksCiName for-imc-je2ytppo
```

Output: 
```
{
    "Response": {
        "RequestId": "51d9ea5a-6e9e-4384-88da-84229e212220",
        "EksCiIds": [
            "eksci-bd80pz8s"
        ]
    }
}
```

