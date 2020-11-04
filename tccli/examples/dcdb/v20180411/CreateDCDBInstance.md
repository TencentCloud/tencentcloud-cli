**Example 1: 创建包年包月的分布式数据库实例**



Input: 

```
tccli dcdb CreateDCDBInstance --cli-unfold-argument  \
    --ShardMemory 2\
    --ShardStorage 10\
    --ShardNodeCount 3\
    --ShardCount 2\
    --DbVersionId 5.7.17\
    --Count 1\
    --Period 1\
    --Zones ap-guangzhou-2 ap-guangzhou-2\
    --AutoVoucher true
```

Output: 
```
{
    "Response": {
        "RequestId": "8c4fba95-01e4-61d9-4146-59fc5afdf962",
        "DealName": "20181103110163",
        "InstanceIds": [
            "dcdbt-avw0207d"
        ]
    }
}
```

