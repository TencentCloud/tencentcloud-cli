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
    --UserSubnetIPNum 42 \
    --Type sp_cdwch_cn \
    --Zone ap-chongqing-1 \
    --UserVPCId vpc-om1fv1n7 \
    --UserSubnetId subnet-76jchjca \
    --ProductVersion 2.0.0_REL \
    --InstanceName 我的TCHouse-X实例 \
    --Case create_instance \
    --Resources.0.Component impalad \
    --Resources.0.Cpu 4 \
    --Resources.0.DeployMode 0 \
    --Resources.0.Memory 16 \
    --Resources.0.SpecName 2X-Small \
    --Resources.0.Count 1 \
    --Resources.0.VirtualClusterName 我的Warehouse \
    --Resources.1.Component impalad \
    --Resources.1.DeployMode 2 \
    --Resources.1.SpecName CLB \
    --Resources.1.Cpu 0 \
    --Resources.1.Memory 0 \
    --Resources.1.VirtualClusterName 我的Warehouse \
    --Resources.1.Count 1 \
    --VirtualClusterName 我的Warehouse \
    --IsQueryPrice False \
    --InstancePwd  \
    --SparkSpec.DriverCores 0 \
    --SparkSpec.ExecutorCores 0 \
    --SparkSpec.ExecutorNum 0 \
    --OfflineTaskLimit 5 \
    --SupportLoginType 2 1 \
    --CipherMode 1 \
    --TCLakeSpec.CatalogType LAKEHOUSE \
    --TCLakeSpec.CatalogNameType SYSTEM \
    --CosType 0
```

Output: 
```
{
    "Response": {
        "Type": "",
        "GoodsCategoryId": 0,
        "GoodsDetailStr": "{\"TimeSpan\":1,\"Type\":\"\",\"context\":{\"AppID\":1375622477,\"Case\":\"create_instance\",\"ChargeProperties\":{\"ChargeType\":\"POSTPAID_BY_HOUR\",\"RenewFlag\":0,\"TimeSpan\":1,\"TimeUnit\":\"h\"},\"CipherMode\":1,\"ClusterType\":0,\"CosType\":0,\"DealName\":\"\",\"ExpiredTime\":\"3020-12-23 23:59:59\",\"GracefulEnable\":false,\"HourToPrepaid\":false,\"InstanceID\":\"instance-eqvmsxd7\",\"InstanceName\":\"我的TCHouse-X实例\",\"InstanceType\":\"warehouse\",\"KernelKey\":\"5a84f37b-1827-41dd-b15f-bf80a400\",\"Kind\":\"external\",\"KmsId\":\"\",\"LdapConfig\":null,\"ManagePwd\":\"cGRqWk1GMjI5QA==\",\"OfflineTaskLimit\":5,\"OperateUin\":\"100044265764\",\"Password\":\"Zm9mUkFZODk5LQ==\",\"Region\":\"ap-chongqing\",\"ResourceAG\":\"ag-kctmqu5t\",\"ResourceAppID\":1305504398,\"ResourceOperateUin\":\"100018492051\",\"ResourceServiceSubnetID\":\"subnet-mr53p0m8\",\"ResourceSubnetID\":\"subnet-3pgouhxc\",\"ResourceUin\":\"100018492051\",\"ResourceVPCID\":\"vpc-975qib7h\",\"Resources\":[{\"AddResourceTag\":false,\"Component\":\"impalad\",\"Count\":1,\"Cpu\":4,\"DeployMode\":0,\"Id\":0,\"InstanceType\":\"\",\"K8sResourceName\":\"\",\"Memory\":16,\"Nvme\":true,\"Region\":\"\",\"RequestCpu\":3,\"RequestMemory\":12,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"2X-Small\",\"Storage\":0,\"VirtualCluster\":\"vw-5v1x8wyy\",\"VirtualClusterName\":\"我的Warehouse\",\"WarehouseType\":0},{\"AddResourceTag\":false,\"Component\":\"impalad\",\"Count\":1,\"Cpu\":0,\"DeployMode\":2,\"Id\":0,\"InstanceType\":\"\",\"K8sResourceName\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"\",\"RequestCpu\":0,\"RequestMemory\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"CLB\",\"Storage\":0,\"VirtualCluster\":\"vw-5v1x8wyy\",\"VirtualClusterName\":\"我的Warehouse\",\"WarehouseType\":0},{\"AddResourceTag\":false,\"Component\":\"cfs\",\"Count\":1,\"Cpu\":0,\"DeployMode\":1,\"Id\":12,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"ap-guangzhou,ap-chongqing,ap-shanghai,ap-singapore,ap-beijing\",\"RequestCpu\":0,\"RequestMemory\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"CFS-SD\",\"Storage\":1000,\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0},{\"AddResourceTag\":false,\"Component\":\"access-server\",\"Count\":2,\"Cpu\":8,\"DeployMode\":0,\"Id\":14,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"Memory\":32,\"Nvme\":false,\"Region\":\"ap-singapore,ap-chongqing,ap-guangzhou,ap-shanghai,ap-beijing\",\"RequestCpu\":7,\"RequestMemory\":26,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"X-Small\",\"Storage\":0,\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0},{\"AddResourceTag\":false,\"Component\":\"access-server\",\"Count\":1,\"Cpu\":0,\"DeployMode\":2,\"Id\":15,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"ap-singapore,ap-chongqing,ap-guangzhou,ap-shanghai,ap-beijing\",\"RequestCpu\":0,\"RequestMemory\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"CLB\",\"Storage\":0,\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0},{\"AddResourceTag\":false,\"Component\":\"tccatalog\",\"Count\":1,\"Cpu\":0,\"DeployMode\":1,\"Id\":19,\"InstanceType\":\"warehouse\",\"K8sResourceName\":\"\",\"Memory\":0,\"Nvme\":false,\"Region\":\"ap-chongqing\",\"RequestCpu\":0,\"RequestMemory\":0,\"ServerlessVirtualCluster\":\"\",\"SpecName\":\"TCCATALOG\",\"Storage\":0,\"VirtualCluster\":\"default-cluster\",\"VirtualClusterName\":\"default-cluster\",\"WarehouseType\":0}],\"SecurityGroupID\":\"sg-38ccv1h0\",\"ServerlessSpec\":null,\"SparkSpec\":null,\"StackID\":\"WAREHOUSE-2.0.0_REL\",\"StorageType\":\"cbs\",\"SupportLoginType\":[2,1],\"TCLakeSpec\":{\"CatalogId\":\"\",\"CatalogName\":\"\",\"CatalogNameType\":\"SYSTEM\",\"CatalogType\":\"LAKEHOUSE\",\"Comment\":\"\",\"EnableDeleteCatalog\":false},\"Tags\":{\"ResourceTags\":null},\"Uin\":\"100043935658\",\"UserDefineCosSpec\":null,\"UserSubnetID\":\"subnet-76jchjca\",\"UserVPCID\":\"vpc-om1fv1n7\",\"VIPType\":0,\"Version\":\"2.0.0_REL\",\"VirtualCluster\":\"vw-5v1x8wyy\",\"VirtualClusterName\":\"我的Warehouse\",\"WarehouseType\":0,\"Zone\":\"ap-chongqing-1\",\"ZoneId\":190001},\"curDeadline\":\"3020-12-23 23:59:59\",\"goodsNum\":1,\"newConfig\":null,\"oldConfig\":null,\"pid\":0,\"productCode\":\"\",\"productInfo\":[{\"name\":\"地域\",\"value\":\"重庆\"},{\"name\":\"可用区\",\"value\":\"重庆一区\"}],\"resourceId\":\"instance-eqvmsxd7\",\"subProductCode\":\"\",\"sv_cdwch_a_compute_cu\":20,\"timeUnit\":\"h\"}",
        "GoodsDetail": "",
        "GoodsNum": 1,
        "PayMode": 0,
        "RegionId": 19,
        "ZoneId": 190001,
        "ResourceId": "instance-eqvmsxd7",
        "RequestId": "d6e38210-1931-49be-a820-2499c5ff6704",
        "ErrorMsg": ""
    }
}
```

