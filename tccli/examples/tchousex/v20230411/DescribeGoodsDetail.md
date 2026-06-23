**Example 1: 创建实例**

创建实例

Input: 

```
tccli tchousex DescribeGoodsDetail --cli-unfold-argument  \
    --ChargeProperties.TimeSpan 1 \
    --ChargeProperties.TimeUnit h \
    --ChargeProperties.ChargeType POSTPAID_BY_HOUR \
    --ChargeProperties.RenewFlag 0 \
    --InstanceType warehouse \
    --UserSubnetIPNum 87 \
    --Type sp_cdwch_cn \
    --Zone ap-chongqing-1 \
    --UserVPCId vpc-m7r0xr5f \
    --UserSubnetId subnet-2y60gine \
    --ProductVersion 2.2.2_AI_FUC_TEST \
    --InstanceName 我的TCHouse-X实例 \
    --Case create_instance \
    --VirtualClusterName 我的Warehouse \
    --IsQueryPrice False \
    --TCLakeSpec.CatalogType LAKEHOUSE \
    --TCLakeSpec.CatalogNameType SYSTEM \
    --TCIMode 1 \
    --WarehouseType 0 \
    --SupportLoginType 2 \
    --CipherMode 1 \
    --Resources.0.Component impalad \
    --Resources.0.Cpu 16 \
    --Resources.0.DeployMode 0 \
    --Resources.0.Memory 64 \
    --Resources.0.SpecName Small \
    --Resources.0.Count 1 \
    --Resources.0.VirtualClusterName 我的Warehouse \
    --Resources.1.Component impalad \
    --Resources.1.DeployMode 2 \
    --Resources.1.SpecName CLB \
    --Resources.1.Cpu 0 \
    --Resources.1.Memory 0 \
    --Resources.1.VirtualClusterName 我的Warehouse \
    --Resources.1.Count 1
```

Output: 
```
{
    "Response": {
        "Type": "sp_tchouse_x_v2",
        "GoodsCategoryId": 2023483,
        "GoodsDetailStr": "{\"TimeSpan\":1,\"Type\":\"sp_tchouse_x_v2\",\"context\":{\"AppID\":1375622477,\"BillResourceMode\":0,\"Case\":\"create_instance\",\"ChargeProperties\":{\"ChargeType\":\"POSTPAID_BY_HOUR\",\"RenewFlag\":0,\"TimeSpan\":1,\"TimeUnit\":\"h\"},\"CipherMode\":1,\"ClusterType\":0,\"Component\":\"\",\"CosType\":0,\"DealName\":\"\",\"DealOrderCallback\":false,\"EnableSSL\":false,\"ExpiredTime\":\"3020-12-23 23:59:59\",\"GracefulEnable\":false,\"HourToPrepaid\":false,\"ImageId\":\"\",\"InstanceID\":\"instance-n253yiyh\",\"InstanceName\":\"我的TCHouse-X实例\",\"InstanceResourceMode\":\"\",\"InstanceType\":\"warehouse\",\"InstanceUpgradeTaskId\":0,\"IsSecondaryZone\":false,\"KernelKey\":\"0c241f08-3ba5-4a8d-9baf-36a3cb9d\",\"Kind\":\"external\",\"KmsId\":\"\",\"LdapConfig\":null,\"ManagePwd\":\"bG1sQU5WMjc2Kg==\",\"MultiZones\":[\"ap-chongqing-1\"],\"OfflineTaskLimit\":0,\"OperateUin\":\"100044265764\",\"OriginalCase\":\"create_instance\",\"Password\":\"ZnZoWVRLNjM5JQ==\",\"Region\":\"ap-chongqing\",\"ResourceAppID\":1305504398,\"ResourceOperateUin\":\"100018492051\",\"ResourceServiceSubnetID\":\"subnet-q1ye68w0\",\"ResourceSubnetID\":\"subnet-5p0k8q5m\",\"ResourceUin\":\"100018492051\",\"ResourceVPCID\":\"vpc-b9vw8r3x\",\"Resources\":[{\"AddResourceTag\":false,\"Component\":\"impalad\",\"Count\":1,\"Cpu\":16,\"DeployMode\":0,\"Id\":0,\"InstanceType\":\"\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":64,\"Nvme\":true,\"Region\":\"\",\"RequestCpu\":14,\"RequestMemory\":55,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"Small\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"vw-l1qao6ko\",\"VirtualClusterName\":\"我的Warehouse\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"},{\"AddResourceTag\":false,\"Component\":\"impalad\",\"Count\":1,\"Cpu\":0,\"DeployMode\":2,\"Id\":0,\"InstanceType\":\"\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"\",\"RequestCpu\":0,\"RequestMemory\":0,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"CLB\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"vw-l1qao6ko\",\"VirtualClusterName\":\"我的Warehouse\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"},{\"AddResourceTag\":false,\"Component\":\"access-server\",\"Count\":2,\"Cpu\":8,\"DeployMode\":0,\"Id\":14,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":32,\"Nvme\":false,\"Region\":\"ap-guangzhou,ap-chongqing,ap-shanghai,ap-singapore,ap-beijing,ap-hongkong\",\"RequestCpu\":7,\"RequestMemory\":26,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"X-Small\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"},{\"AddResourceTag\":false,\"Component\":\"access-server\",\"Count\":1,\"Cpu\":0,\"DeployMode\":2,\"Id\":15,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"ap-guangzhou,ap-chongqing,ap-shanghai,ap-singapore,ap-beijing,ap-hongkong\",\"RequestCpu\":0,\"RequestMemory\":0,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"CLB\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"},{\"AddResourceTag\":false,\"Component\":\"livy-meson\",\"Count\":1,\"Cpu\":4,\"DeployMode\":0,\"Id\":17,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":8,\"Nvme\":false,\"Region\":\"ap-guangzhou,ap-chongqing,ap-shanghai,ap-singapore,ap-beijing,ap-hongkong\",\"RequestCpu\":3,\"RequestMemory\":5,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"2X-Small\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"},{\"AddResourceTag\":false,\"Component\":\"livy-meson\",\"Count\":1,\"Cpu\":0,\"DeployMode\":2,\"Id\":18,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"ap-guangzhou,ap-chongqing,ap-shanghai,ap-singapore,ap-beijing,ap-hongkong\",\"RequestCpu\":0,\"RequestMemory\":0,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"CLB\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"},{\"AddResourceTag\":false,\"Component\":\"tccatalog\",\"Count\":1,\"Cpu\":0,\"DeployMode\":1,\"Id\":19,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"LastPushTimeNew\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"ap-guangzhou,ap-chongqing,ap-shanghai,ap-singapore,ap-beijing,ap-hongkong\",\"RequestCpu\":0,\"RequestMemory\":0,\"ResourceUsageRecordId\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"TCCATALOG\",\"Storage\":0,\"UsageEnd\":\"\",\"UsageStart\":\"\",\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0,\"WarehouseUsageResourceType\":\"\"}],\"SRContext\":null,\"SRInstanceIds\":\"\",\"SRParams\":null,\"SecondaryZoneInfo\":null,\"SecurityGroupID\":\"sg-38ccv1h0\",\"ServerlessSpec\":null,\"SparkSpec\":null,\"StackID\":\"WAREHOUSE-2.2.2_REL\",\"StorageType\":\"cbs\",\"SupportLoginType\":[2],\"TCIInstanceSpec\":null,\"TCIMode\":1,\"TCLakeSpec\":{\"CatalogId\":\"\",\"CatalogName\":\"\",\"CatalogNameType\":\"SYSTEM\",\"CatalogType\":\"LAKEHOUSE\",\"Comment\":\"\",\"EnableDeleteCatalog\":false},\"Tags\":{\"ResourceTags\":null},\"Uin\":\"100043935658\",\"UpgradeVersion\":\"\",\"UserDefineCosSpec\":null,\"UserSubnetID\":\"subnet-2y60gine\",\"UserVPCID\":\"vpc-m7r0xr5f\",\"VIPType\":0,\"Version\":\"2.2.2_AI_FUC_TEST\",\"VirtualCluster\":\"vw-l1qao6ko\",\"VirtualClusterName\":\"我的Warehouse\",\"WarehouseType\":0,\"Zone\":\"ap-chongqing-1\",\"ZoneId\":190001},\"curDeadline\":\"3020-12-23 23:59:59\",\"goodsNum\":1,\"instanceType\":\"\",\"newConfig\":null,\"oldConfig\":null,\"pid\":1053762,\"productCode\":\"p_tchouse_x\",\"productInfo\":[{\"name\":\"地域\",\"value\":\"重庆\"},{\"name\":\"可用区\",\"value\":\"重庆一区\"}],\"resourceId\":\"instance-n253yiyh\",\"subProductCode\":\"sp_tchouse_x_v2\",\"sv_tchouse_x_warehouse_hp\":16,\"timeUnit\":\"h\"}",
        "GoodsDetail": "",
        "GoodsNum": 1,
        "PayMode": 0,
        "RegionId": 19,
        "ZoneId": 190001,
        "ResourceId": "instance-n253yiyh",
        "RequestId": "c67a4e05-cbf7-4a62-9fba-50334964ff8c",
        "ErrorMsg": ""
    }
}
```

