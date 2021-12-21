**Example 1: 创建公网数据迁移任务**

将用户的mysql公网实例数据, 采用全量方式迁移到腾讯云上海地域的cdb-e78e0nnv实例上. 其中源实例的接入地域为广州. 数据一致性检查做全量检测.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 设置为一个方便辨识的名称 \
    --SrcDatabaseType mysql \
    --SrcAccessType extranet \
    --SrcInfo.Supplier others \
    --SrcInfo.Ip 14.17.22.36 \
    --SrcInfo.Region ap-guangzhou \
    --SrcInfo.User root \
    --SrcInfo.Password yourPassword \
    --SrcInfo.Port 3306 \
    --DstDatabaseType mysql \
    --DstAccessType cdb \
    --DstInfo.InstanceId cdb-e78e0nnv \
    --DstInfo.Region ap-shanghai \
    --DstInfo.ReadOnly 0 \
    --DstInfo.User root \
    --DstInfo.Password yourPassword \
    --DatabaseInfo [] \
    --Tags.0.TagKey 负责人 \
    --Tags.0.TagValue bob \
    --MigrateOption.ExternParams {} \
    --MigrateOption.MigrateObject 1 \
    --MigrateOption.RunMode 1 \
    --MigrateOption.ExpectTime 2020-09-22 00:00:00 \
    --MigrateOption.ConsistencyType 2 \
    --MigrateOption.MigrateType 2 \
    --MigrateOption.IsOverrideRoot 0
```

Output: 
```
{
    "Response": {
        "JobId": "dts-1kl0iy0v",
        "RequestId": "2201c42a-714f-4faa-915b-a51cc09f5cec"
    }
}
```

**Example 2: 创建专线数据迁移任务**

将用户通过专线接入的mysql实例,  全量+增量迁移迁移到腾讯云上海地域的cdb-d0dqi8nv实例上. 其中源实例的接入地域为广州.

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 设置为一个方便辨识的名称 \
    --SrcDatabaseType mysql \
    --SrcAccessType dcg \
    --SrcInfo.Supplier others \
    --SrcInfo.UniqDcgId dcg-cyrjcc09 \
    --SrcInfo.VpcId vpc-72jblfaa \
    --SrcInfo.SubnetId subnet-7raec42a \
    --SrcInfo.Ip 192.168.120.136 \
    --SrcInfo.Region ap-guangzhou \
    --SrcInfo.User root \
    --SrcInfo.Password yourPassword \
    --SrcInfo.Port 3306 \
    --DstDatabaseType mysql \
    --DstAccessType cdb \
    --DstInfo.InstanceId cdb-d0dqi8nv \
    --DstInfo.Region ap-shanghai \
    --DstInfo.ReadOnly 0 \
    --DstInfo.User root \
    --DstInfo.Password yourPassword \
    --DatabaseInfo [{"Database":"test","Table":["user","log"]}] \
    --Tags.0.TagKey 负责人 \
    --Tags.0.TagValue bob \
    --MigrateOption.ExternParams {} \
    --MigrateOption.MigrateObject 1 \
    --MigrateOption.RunMode 1 \
    --MigrateOption.ExpectTime 2020-09-22 00:00:00 \
    --MigrateOption.ConsistencyType 2 \
    --MigrateOption.MigrateType 2 \
    --MigrateOption.IsOverrideRoot 0
```

Output: 
```
{
    "Response": {
        "JobId": "dts-o3s1vxsp",
        "RequestId": "915bc42a-714f-4faa-915b-a51cc09f5714"
    }
}
```

**Example 3: 创建云数据库迁移任务**

从腾讯云mysql实例结构迁移到腾讯云另一个mysql实例，选择部分库表做，不做数据一致性检查。

Input: 

```
tccli dts CreateMigrateJob --cli-unfold-argument  \
    --JobName 设置为一个方便辨识的名称 \
    --SrcDatabaseType mysql \
    --SrcAccessType cdb \
    --SrcInfo.Supplier others \
    --SrcInfo.InstanceId cdb-ieow93923 \
    --SrcInfo.User root \
    --SrcInfo.Password yourPassword \
    --DstDatabaseType mysql \
    --DstAccessType cdb \
    --DstInfo.InstanceId cdb-e78e0nnv \
    --DstInfo.Region ap-shanghai \
    --DstInfo.ReadOnly 0 \
    --DstInfo.User root \
    --DstInfo.Password yourPassword \
    --DatabaseInfo [] \
    --Tags.0.TagKey 负责人 \
    --Tags.0.TagValue bob \
    --MigrateOption.ExternParams {} \
    --MigrateOption.MigrateObject 1 \
    --MigrateOption.RunMode 1 \
    --MigrateOption.ExpectTime 2020-09-22 00:00:00 \
    --MigrateOption.ConsistencyType 5 \
    --MigrateOption.MigrateType 2 \
    --MigrateOption.IsOverrideRoot 0
```

Output: 
```
{
    "Response": {
        "JobId": "dts-46i7easd",
        "RequestId": "bc94c57b-9d69-11e9-84cb-256e968056b0"
    }
}
```

