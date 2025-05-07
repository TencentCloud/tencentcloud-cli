**Example 1: describe creator**



Input: 

```
tccli wedata DescribeTenantProjects --cli-unfold-argument  \
    --PageNumber 0 \
    --DescribeCreator true \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 1,
            "Rows": [
                {
                    "TenantId": "1",
                    "ProjectId": "1990",
                    "ProjectName": "admin",
                    "DisplayName": "admin",
                    "Region": "beijing",
                    "Description": "beijing",
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "Creator": {
                        "UserId": "199199",
                        "UserName": "zhangsan",
                        "DisplayName": "zhangsan"
                    },
                    "Tenant": {
                        "TenantId": "1",
                        "TenantName": "zhangsan",
                        "DisplayName": "zhangsan",
                        "Description": "zhangsan",
                        "OwnerUserId": "zhangsan",
                        "Params": "zhangsan"
                    },
                    "AdminUsers": [
                        {
                            "UserId": "1999",
                            "UserName": "zhangsan",
                            "DisplayName": "zhangsan"
                        }
                    ],
                    "Clusters": [
                        {
                            "ClusterId": "zhangsan",
                            "ClusterType": "zhangsan",
                            "ClusterName": "zhangsan",
                            "RegionCn": "zhangsan",
                            "RegionEn": "zhangsan",
                            "RegionArea": "zhangsan",
                            "Used": true,
                            "Status": 1,
                            "StatusInfo": "zhangsan",
                            "StorageType": "zhangsan",
                            "ComputeType": "zhangsan",
                            "ClusterResource": "zhangsan",
                            "ChargeType": "zhangsan",
                            "CreateTime": "2020-09-22T00:00:00+00:00",
                            "ExtraConf": "zhangsan",
                            "RangerUserName": "zhangsan",
                            "CdwUserName": "zhangsan"
                        }
                    ],
                    "Params": "zhangsan",
                    "Status": 1
                }
            ],
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "zhangsan"
    }
}
```

