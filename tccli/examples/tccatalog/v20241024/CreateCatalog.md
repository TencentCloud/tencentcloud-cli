**Example 1: 创建数据目录**

创建数据目录

Input: 

```
tccli tccatalog CreateCatalog --cli-unfold-argument  \
    --Name HiveCatalog \
    --Type EMR-HIVE \
    --Comment Hive数据目录 \
    --Connection.MysqlConnection.InstanceId  \
    --Connection.MysqlConnection.InstanceName  \
    --Connection.MysqlConnection.JDBCUrl  \
    --Connection.MysqlConnection.User  \
    --Connection.MysqlConnection.Password  \
    --Connection.MysqlConnection.NetWork.VpcId  \
    --Connection.MysqlConnection.NetWork.VpcCidrBlock  \
    --Connection.MysqlConnection.NetWork.SubnetId  \
    --Connection.MysqlConnection.NetWork.SubnetCidrBlock  \
    --Connection.EmrHiveConnection.InstanceId dsadhh-edsd-dsad-eew \
    --Connection.EmrHiveConnection.InstanceName test-hive \
    --Connection.EmrHiveConnection.MetaStoreUrl thrift://127.0.0.1:9083 \
    --Connection.EmrHiveConnection.NetWork.VpcId vpc-test \
    --Connection.EmrHiveConnection.NetWork.VpcCidrBlock 10.0.0.1/12 \
    --Connection.EmrHiveConnection.NetWork.SubnetId subnet-test \
    --Connection.EmrHiveConnection.NetWork.SubnetCidrBlock 10.0.0.1/24 \
    --Connection.TCHouseDConnection.InstanceId  \
    --Connection.TCHouseDConnection.InstanceName  \
    --Connection.TCHouseDConnection.JDBCUrl  \
    --Connection.TCHouseDConnection.User  \
    --Connection.TCHouseDConnection.Password  \
    --Connection.TCHouseDConnection.NetWork.VpcId  \
    --Connection.TCHouseDConnection.NetWork.VpcCidrBlock  \
    --Connection.TCHouseDConnection.NetWork.SubnetId  \
    --Connection.TCHouseDConnection.NetWork.SubnetCidrBlock  \
    --Connection.DlcConnection.InstanceId  \
    --Connection.DlcConnection.InstanceName  \
    --Connection.VolumeConnection.Location  \
    --Connection.TccHiveConnection.EndpointServiceId  \
    --Connection.TccHiveConnection.MetaStoreUrl  \
    --Connection.TccHiveConnection.HiveVersion  \
    --Connection.TccHiveConnection.Location  \
    --Connection.TccHiveConnection.NetWork.VpcId  \
    --Connection.TccHiveConnection.NetWork.VpcCidrBlock  \
    --Connection.TccHiveConnection.NetWork.SubnetId  \
    --Connection.TccHiveConnection.NetWork.SubnetCidrBlock  \
    --Connection.WeDataModelConnection.SyncInterval  \
    --Connection.WeDataModelConnection.TargetSchema  \
    --Connection.WeDataModelConnection.ServerId 
```

Output: 
```
{
    "Response": {
        "CatalogId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

