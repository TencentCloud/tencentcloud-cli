**Example 1: 查询OnCvm双节点的新购计费参数**

查询OnCvm双节点的新购计费参数

Input: 

```
tccli sqlserver DescribeInstanceTradeParameter --cli-unfold-argument  \
    --Zone ap-guangzhou-6 \
    --InstanceChargeType PREPAID \
    --InstanceType cvmHA \
    --Memory 4 \
    --Storage 200 \
    --GoodsNum 1 \
    --SubnetId subnet-15y3y4eo \
    --VpcId vpc-hqxhp43z \
    --Period 1 \
    --DBVersion 2008R2 \
    --AutoRenewFlag 1 \
    --Weekly 1 3 5 \
    --StartTime 01:00 \
    --Span 3 \
    --MultiZones true \
    --Cpu 2 \
    --MachineType CLOUD_BSSD
```

Output: 
```
{
    "Response": {
        "Parameter": "{\"uin\":\"2919041563\",\"ownerUin\":\"2919041563\",\"appId\":251000111,\"goods\":[{\"goodsCategoryId\":1025890,\"goodsNum\":1,\"payMode\":1,\"regionId\":1,\"zoneId\":100006,\"goodsDetail\":{\"pid\":1019180,\"productCode\":\"p_sqlserver\",\"subProductCode\":\"sp_sqlserver_dual_exclusive_cloud\",\"timeSpan\":1,\"timeUnit\":\"m\",\"productInfo\":[{\"name\":\"项目\",\"value\":\"default project\"},{\"name\":\"配置\",\"value\":\"4GB内存，200GB存储空间，0次每秒，SQL Server 2008R2\"},{\"name\":\"实例版本\",\"value\":\"双机高可用\"},{\"name\":\"地域\",\"value\":\"广州\"},{\"name\":\"所属网络\",\"value\":\"三区专属\"},{\"name\":\"可用区\",\"value\":\"广州六区\"},{\"name\":\"RequestSource\",\"value\":\"API\"}],\"autoRenewFlag\":1,\"goodsNum\":1,\"type\":\"CLOUD_BSSD\",\"version\":\"2008R2\",\"subnetId\":1604224,\"vpcId\":74483,\"model\":3,\"weekly\":[1,3,5],\"startTime\":\"01:00\",\"span\":3,\"RoGroupForcedUpgrade\":0,\"ResourceTags\":null,\"waitSwitch\":1,\"ExtParam\":{\"token\":\"\",\"useragent\":\"\",\"referer\":\"\",\"from\":\"\"},\"collation\":\"Chinese_PRC_CI_AS\",\"timeZone\":\"China Standard Time\",\"sv_sqlserver_cpu_dual_exclusive_cloud_enterprise\":2,\"sv_sqlserver_cpu_dual_exclusive_cloud_standard\":0,\"sv_sqlserver_mem_dual_exclusive_cloud_enterprise\":4,\"sv_sqlserver_mem_dual_exclusive_cloud_standard\":0,\"sv_sqlserver_disk_dual_enhancedssd\":0,\"sv_sqlserver_disk_dual_fastssd\":0,\"sv_sqlserver_disk_dual_universalssd\":200},\"platform\":1,\"projectId\":0}]}\n",
        "RequestId": "2a2c00b5-77a8-4eda-be01-3f58230da22e"
    }
}
```

