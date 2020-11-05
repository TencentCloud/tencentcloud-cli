**Example 1: Querying the price of instance creation**



Input: 

```
tccli emr InquiryPriceCreateInstance --cli-unfold-argument  \
    --SupportHA 0\
    --PayMode 0\
    --Placement.Zone ap-guangzhou-3\
    --Placement.ProjectId 0\
    --Software hadoop-2.7.3 zookeeper-3.4.9 hive-2.3.2 knox-1.2.0\
    --ResourceSpec.MasterResourceSpec.MemSize 16384\
    --ResourceSpec.MasterResourceSpec.Cpu 4\
    --ResourceSpec.MasterResourceSpec.DiskSize 100\
    --ResourceSpec.MasterResourceSpec.DiskType CLOUD_PREMIUM\
    --ResourceSpec.MasterResourceSpec.Spec CVM.S3\
    --ResourceSpec.MasterResourceSpec.RootSize 100\
    --ResourceSpec.MasterResourceSpec.StorageType 5\
    --ResourceSpec.CoreResourceSpec.MemSize 16384\
    --ResourceSpec.CoreResourceSpec.Cpu 4\
    --ResourceSpec.CoreResourceSpec.DiskSize 100\
    --ResourceSpec.CoreResourceSpec.DiskType CLOUD_PREMIUM\
    --ResourceSpec.CoreResourceSpec.Spec CVM.S3\
    --ResourceSpec.CoreResourceSpec.RootSize 100\
    --ResourceSpec.CoreResourceSpec.StorageType 5\
    --ResourceSpec.MasterCount 1\
    --ResourceSpec.CoreCount 2\
    --VPCSettings.VpcId vpc-ezt5qmqz\
    --VPCSettings.SubnetId subnet-jhgsahx0\
    --TimeSpan 3600\
    --TimeUnit s\
    --Currency CNY\
    --ProductId 2
```

Output: 
```
{
    "Response": {
        "DiscountCost": 5.53,
        "OriginalCost": 7.87,
        "RequestId": "863e0be5-ab86-4daa-84f2-f84953f18aec",
        "TimeSpan": 3600,
        "TimeUnit": "s"
    }
}
```

