**Example 1: 创建容器实例**



Input: 

```
tccli tke CreateEKSContainerInstances --cli-unfold-argument  \
    --AutoCreateEipAttribute.InternetMaxBandwidthOut 1 \
    --AutoCreateEipAttribute.DeletePolicy Immediate \
    --AutoCreateEipAttribute.InternetServiceProvider BGP \
    --CamRoleName xx \
    --VpcId vpc-12345678 \
    --DnsConfig.Nameservers xx \
    --DnsConfig.Searches xx \
    --DnsConfig.Options.0.Name xx \
    --DnsConfig.Options.0.Value xx \
    --Replicas 1 \
    --ImageRegistryCredentials.0.Username xx \
    --ImageRegistryCredentials.0.Password xx \
    --ImageRegistryCredentials.0.Name xx \
    --ImageRegistryCredentials.0.Server xx \
    --EksCiVolume.CbsVolumes.0.CbsDiskId xx \
    --EksCiVolume.CbsVolumes.0.Name xx \
    --EksCiVolume.NfsVolumes.0.Path xx \
    --EksCiVolume.NfsVolumes.0.ReadOnly True \
    --EksCiVolume.NfsVolumes.0.Name xx \
    --EksCiVolume.NfsVolumes.0.Server xx \
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
    --Containers.0.Name xx \
    --Containers.0.GpuLimit 1 \
    --Containers.0.WorkingDir xx \
    --Containers.0.Image xx \
    --Containers.0.Args 10000 \
    --Containers.0.VolumeMounts.0.MountPropagation xx \
    --Containers.0.VolumeMounts.0.ReadOnly True \
    --Containers.0.VolumeMounts.0.MountPath xx \
    --Containers.0.VolumeMounts.0.SubPath xx \
    --Containers.0.VolumeMounts.0.Name xx \
    --Containers.0.RestartCount 1 \
    --Containers.0.EnvironmentVars.0.Name xx \
    --Containers.0.EnvironmentVars.0.Value xx \
    --Containers.0.Memory 0.0 \
    --Containers.0.Cpu 0.0 \
    --EksCiName xx
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

