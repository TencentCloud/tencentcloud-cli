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
                    "ExtraConf": "abc",
                    "RangerUserName": "abc",
                    "CdwUserName": "abc"
                }
            ],
            "Params": "abc",
            "Status": 1,
            "Model": "abc"
        },
        "RequestId": "abc"
    }
}
```

