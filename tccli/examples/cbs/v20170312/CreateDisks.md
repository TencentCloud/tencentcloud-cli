**Example 1: Purchasing a cloud disk with basic parameters**

This example shows you how to purchase a 50-GB HDD cloud disk in Guangzhou Zone 2 for one month with upfront payment, assign it to the project “0”, get a notification upon expiration and configure it for automatic renewal.

Input: 

```
tccli cbs CreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_BASIC \
    --DiskCount 1 \
    --DiskSize 50 \
    --Placement.Zone ap-guangzhou-2 \
    --Placement.ProjectId 0 \
    --DiskChargeType PREPAID \
    --DiskChargePrepaid.Period 1 \
    --DiskChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
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

**Example 2: Creating a pay-as-you-go cloud disk billed hourly**

This example shows you how to create a pay-as-you-go 100 GB premium cloud disk billed hourly in Guangzhou Zone 3.

Input: 

```
tccli cbs CreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_PREMIUM \
    --DiskCount 1 \
    --Placement.Zone ap-guangzhou-3 \
    --Placement.ProjectId 0 \
    --DiskChargeType POSTPAID_BY_HOUR \
    --DiskName postPayDisk \
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

**Example 3: Creating a cloud disk with a snapshot**

This example shows you how to create a cloud disk by specifying a snapshot without specifying `DiskSize`. In this example, the size of the new cloud disk will be the same as that of the snapshot, and the snapshot data will be copied to the new cloud disk.

Input: 

```
tccli cbs CreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_BASIC \
    --DiskCount 1 \
    --SnapshotId snap-iepc4w3h \
    --Placement.Zone ap-guangzhou-2 \
    --Placement.ProjectId 0 \
    --DiskChargeType PREPAID \
    --DiskChargePrepaid.Period 1 \
    --DiskChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
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

