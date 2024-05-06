**Example 1: describe project with params**



Input: 

```
tccli wedata DescribeProject --cli-unfold-argument  \
    --ProjectId 9782035857154610592
```

Output: 
```
{
    "Response": {
        "Data": {
            "TenantId": "abc",
            "ProjectId": "abc",
            "ProjectName": "abc",
            "DisplayName": "abc",
            "Region": "abc",
            "Description": "abc",
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "Creator": {
                "UserId": "abc",
                "UserName": "abc",
                "DisplayName": "abc",
                "PhoneNum": "abc",
                "Email": "abc"
            },
            "Tenant": {
                "TenantId": "abc",
                "TenantName": "abc",
                "DisplayName": "abc",
                "Description": "abc",
                "OwnerUserId": "abc",
                "Params": "abc"
            },
            "AdminUsers": [
                {
                    "UserId": "abc",
                    "UserName": "abc",
                    "DisplayName": "abc",
                    "PhoneNum": "abc",
                    "Email": "abc"
                }
            ],
            "Clusters": [
                {
                    "ClusterId": "abc",
                    "ClusterType": "abc",
                    "ClusterName": "abc",
                    "RegionCn": "abc",
                    "RegionEn": "abc",
                    "RegionArea": "abc",
                    "Used": true,
                    "Status": 1,
                    "StatusInfo": "abc",
                    "StorageType": "abc",
                    "ComputeType": "abc",
                    "ClusterResource": "abc",
                    "ChargeType": "abc",
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "VpcId": "abc",
                    "DescComponents": [
                        "abc"
                    ],
                    "ExtraConf": "abc",
                    "RangerUserName": "abc",
                    "CdwUserName": "abc",
                    "UniqSubnetId": "abc"
                }
            ],
            "Params": "abc",
            "MetaCount": {
                "DatabaseCount": 1
            },
            "Executors": [
                {
                    "ExecutorGroupId": "abc",
                    "ExecutorGroupName": "abc",
                    "ExecutorGroupDesc": "abc",
                    "ExecutorGroupSize": 0,
                    "ExecutorGroupAvailableSize": 0,
                    "ExecutorGroupCreateTime": 0,
                    "Available": true,
                    "Creator": "abc",
                    "ExecutorList": [
                        {
                            "ExecutorVpcId": "abc",
                            "ExecutorIp": "abc",
                            "ExecutorInstanceId": "abc",
                            "ExecutorCreateTime": 0,
                            "Status": "abc",
                            "Health": 0,
                            "ExecutorPort": 0,
                            "Vip": "abc",
                            "Vport": 0,
                            "Priority": 0,
                            "ProjectId": "abc"
                        }
                    ],
                    "Region": "abc",
                    "VpcId": "abc",
                    "RegionEn": "abc",
                    "RegionId": "abc",
                    "ExecutorResourceType": 0
                }
            ],
            "MemberCount": 1,
            "Organizations": [
                {
                    "OrgId": 0
                }
            ],
            "ExecutorGroups": [
                {
                    "ExecutorGroupId": "abc"
                }
            ],
            "ResourcePools": [
                {
                    "ResourcePoolName": "abc",
                    "ResourcePoolId": "abc",
                    "ResourceStatus": 0,
                    "TenantId": "abc",
                    "ProjectId": "abc",
                    "ProjectName": "abc",
                    "RelatedTaskNum": 0,
                    "BindTime": 0,
                    "Description": "abc",
                    "ClusterId": "abc",
                    "ClusterType": "abc",
                    "ResourcePoolType": 0,
                    "StorageType": "abc",
                    "StorageResource": {
                        "Size": 1,
                        "FileNum": 1,
                        "Dir": "abc",
                        "UsedSize": 0,
                        "UsedFileNum": 0
                    },
                    "ComputeType": "abc",
                    "ComputeResource": {
                        "Weight": 0,
                        "MinVCore": 0,
                        "MaxVCore": 0,
                        "MinMemory": 0,
                        "MaxMemory": 0,
                        "MaxAppNum": 0,
                        "MaxAppMasterRatio": 0,
                        "FairSharePreemptionTimeout": 0,
                        "QueueName": "abc",
                        "UsedVCore": 0,
                        "UsedMemory": 0
                    },
                    "UsingTaskNum": 0,
                    "StoragePath": "abc",
                    "ClusterName": "abc"
                }
            ],
            "Status": 1,
            "Model": "abc"
        },
        "RequestId": "abc"
    }
}
```

