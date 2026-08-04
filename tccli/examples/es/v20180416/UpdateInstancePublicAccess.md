**Example 1: ES集群开启kibana公网访问**

用以对开启ES现有集群的kibana公网访问权限

Input: 

```
tccli es UpdateInstancePublicAccess --cli-unfold-argument  \
    --WebNodeTypeInfo.NodeNum 1 \
    --WebNodeTypeInfo.NodeType 1 \
    --KibanaAlteringPublicAccess 1 \
    --MasterNodeType 1 \
    --EsConfigSet.Type 1 \
    --EsConfigSet.EsConfig 1 \
    --NodeNum 1 \
    --EnableCerebro True \
    --MasterNodeDiskSize 1 \
    --CerebroPublicAccess 1 \
    --EsPublicAcl.BlackIpList 1 \
    --EsPublicAcl.WhiteIpList 1 \
    --KibanaPublicAccess 1 \
    --KibanaPrivateAccess 1 \
    --InstanceId 1 \
    --OperationDuration.TimeStart 1 \
    --OperationDuration.TimeZone 1 \
    --OperationDuration.MoreInstances 1 \
    --OperationDuration.Periods 1 \
    --OperationDuration.TimeEnd 1 \
    --BasicSecurityType 0 \
    --CosBackup.IsAutoBackup True \
    --CosBackup.BackupTime 1 \
    --MasterNodeNum 1 \
    --CerebroPrivateAccess 1 \
    --SceneType 0 \
    --Password 1 \
    --ScaleType 0 \
    --NodeInfoList.0.LocalDiskInfo.LocalDiskType 1 \
    --NodeInfoList.0.LocalDiskInfo.LocalDiskSize 1 \
    --NodeInfoList.0.LocalDiskInfo.LocalDiskCount 1 \
    --NodeInfoList.0.NodeType 1 \
    --NodeInfoList.0.DiskEncrypt 1 \
    --NodeInfoList.0.DiskCount 1 \
    --NodeInfoList.0.DiskType 1 \
    --NodeInfoList.0.CpuNum 1 \
    --NodeInfoList.0.NodeNum 1 \
    --NodeInfoList.0.DiskSize 1 \
    --NodeInfoList.0.MemSize 0 \
    --NodeInfoList.0.Type 1 \
    --KibanaPrivatePort 1 \
    --MultiZoneInfo.0.SubnetId 1 \
    --MultiZoneInfo.0.Zone 1 \
    --EsConfig 1 \
    --DiskSize 1 \
    --SwitchPrivateLink 1 \
    --InstanceName 1 \
    --EsAcl.BlackIpList 1 \
    --EsAcl.WhiteIpList 1.1.1.1 \
    --NodeType 1 \
    --PublicAccess 1 \
    --ForceRestart True \
    --KibanaConfig 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "DealName": "1"
    }
}
```

