**Example 1:  查询OnCvm双节点的新购询价计费参数**

 查询OnCvm双节点的新购询价计费参数

Input: 

```
tccli sqlserver DescribeInquiryPriceParameter --cli-unfold-argument  \
    --Zone ap-guangzhou-6 \
    --InstanceChargeType PREPAID \
    --Memory 4 \
    --Storage 200 \
    --Period 1 \
    --GoodsNum 1 \
    --DBVersion 2008R2 \
    --Cpu 2 \
    --InstanceType cvmHA \
    --MachineType CLOUD_BSSD
```

Output: 
```
{
    "Response": {
        "Parameter": "{\"uin\":\"2919041563\",\"ownerUin\":\"2919041563\",\"resInfo\":[{\"goodsCategoryId\":1025890,\"goodsNum\":1,\"payMode\":1,\"regionId\":1,\"zoneId\":100006,\"goodsDetail\":{\"pid\":1019180,\"productCode\":\"p_sqlserver\",\"subProductCode\":\"sp_sqlserver_dual_exclusive_cloud\",\"timeSpan\":1,\"timeUnit\":\"m\",\"goodsSubType\":\"sp_sqlserver_dual_exclusive_cloud\",\"sv_sqlserver_cpu_dual_exclusive_cloud_enterprise\":2,\"sv_sqlserver_cpu_dual_exclusive_cloud_standard\":0,\"sv_sqlserver_mem_dual_exclusive_cloud_enterprise\":4,\"sv_sqlserver_mem_dual_exclusive_cloud_standard\":0,\"sv_sqlserver_disk_dual_enhancedssd\":0,\"sv_sqlserver_disk_dual_fastssd\":0,\"sv_sqlserver_disk_dual_universalssd\":200},\"platform\":1}]}\n",
        "RequestId": "9102a1ed-1062-4c50-98ab-d585a4586852"
    }
}
```

