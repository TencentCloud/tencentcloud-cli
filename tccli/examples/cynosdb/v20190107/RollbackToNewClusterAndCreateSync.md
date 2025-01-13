**Example 1: 回档到新集群并建立同步**

回档到新集群并建立同步

Input: 

```
tccli cynosdb RollbackToNewClusterAndCreateSync --cli-unfold-argument  \
    --ClusterName 克隆集群 \
    --InstanceInitInfos.0.Cpu 1 \
    --InstanceInitInfos.0.DeviceType common \
    --InstanceInitInfos.0.InstanceCount 1 \
    --InstanceInitInfos.0.InstanceType rw \
    --InstanceInitInfos.0.Memory 1 \
    --OriginalClusterId cynosdbmysql-gq7bzqdd \
    --PayMode 0 \
    --RollbackId 89114 \
    --UniqSubnetId subnet-q59n2exe \
    --UniqVpcId vpc-pqka00kr \
    --Zone ap-guangzhou-3 \
    --SrcUserName srcAccount \
    --SrcPassword 123@abc \
    --DstUserName dstAccount \
    --DstPassword 456@def \
    --DtsPayMode PostPay \
    --DtsTimeSpan 3 \
    --AutoDeleteTencentDb False \
    --Specification Standard \
    --InstanceClass medium \
    --JobName 同步任务 \
    --JobMode fullMode \
    --RunMode Immediate \
    --InitType None \
    --DealOfExistSameTable ReportErrorAfterCheck \
    --ConflictHandleType ReportError \
    --OpTypes Insert Update Delete DDL \
    --StartPosition 2024-12-19T10:11:52+08:00
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "20190522112290"
        ],
        "ClusterIds": [
            "cynosdbmysql-5bmowyzv"
        ],
        "DealNames": [
            "20241223454002457011771"
        ],
        "RequestId": "48b7cd8a-f6dd-4e47-a78a-f23e",
        "ResourceIds": [
            "cynosdbmysql-ins-2jieqil4"
        ],
        "TranId": "20241223454002457011781"
    }
}
```

