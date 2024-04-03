**Example 1: 使用基本参数购买**

新购云盘具体配置如下：云盘所在位置为广州二区，云盘大小50GB，云盘类型为普通云盘，所属项目ID为0，付费模式为预付费，购买时长1个月，通知过期且自动续费。

Input: 

```
tccli cbs CreateDisks --cli-unfold-argument  \
    --Placement.ProjectId 0 \
    --Placement.Zone ap-guangzhou-2 \
    --DiskChargeType PREPAID \
    --DiskCount 1 \
    --DiskType CLOUD_HSSD \
    --ThroughputPerformance 100 \
    --DiskSize 500 \
    --DiskChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --DiskChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "DiskIdSet": [
            "disk-lzrg2pwi"
        ],
        "RequestId": "6a57da9a-2049-7182-2de3-5a1f8014ccfd"
    }
}
```

**Example 2: 根据快照新建云硬盘**

传入快照创建云硬盘，未传DiskSize参数，此时新购云盘的大小为快照大小，新购云盘复制了快照数据。

Input: 

```
tccli cbs CreateDisks --cli-unfold-argument  \
    --Placement.ProjectId 0 \
    --Placement.Zone ap-guangzhou-2 \
    --DiskChargeType PREPAID \
    --DiskCount 1 \
    --DiskType CLOUD_BASIC \
    --DiskChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --DiskChargePrepaid.Period 1 \
    --SnapshotId snap-iepc4w3h
```

Output: 
```
{
    "Response": {
        "DiskIdSet": [
            "disk-6rz0ilvu"
        ],
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6"
    }
}
```

**Example 3: 创建按小时后付费云盘**

在广州三区创建一块云硬盘，云盘类型为高性能云硬盘，大小100GB，付费类型为按小时后付费。

Input: 

```
tccli cbs CreateDisks --cli-unfold-argument  \
    --DiskName postPayDisk \
    --Placement.ProjectId 0 \
    --Placement.Zone ap-guangzhou-3 \
    --DiskChargeType POSTPAID_BY_HOUR \
    --DiskCount 1 \
    --DiskType CLOUD_PREMIUM \
    --DiskSize 100
```

Output: 
```
{
    "Response": {
        "DiskIdSet": [
            "disk-ecjc4cpw"
        ],
        "RequestId": "fe2274fa-eaec-4009-807b-6ffc00963fec"
    }
}
```

