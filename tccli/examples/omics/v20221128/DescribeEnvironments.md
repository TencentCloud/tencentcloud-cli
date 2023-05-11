**Example 1: 查询环境列表**

查询环境列表。

Input: 

```
tccli omics DescribeEnvironments --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Environments": [
            {
                "Available": true,
                "CreationTime": "2022-12-14T16:14:49+08:00",
                "Description": "test description",
                "EnvironmentId": "env-lljckw12",
                "LastWorkflowUuid": "94922fcd-107e-4220-9a0f-cc3cd84a9a27",
                "Message": "",
                "Name": "test",
                "Region": "ap-guangzhou",
                "ResourceIds": {
                    "CFSId": "cfs-iwee8gk3",
                    "CFSStorageType": "SD",
                    "CVMId": "ins-jcbptifa",
                    "EKSId": "cls-9j9zh13o",
                    "SecurityGroupId": "sg-gzsfk3r5",
                    "SubnetId": "subnet-qdkfn4xe",
                    "TDSQLCId": "cynosdbmysql-kzwghvxj",
                    "VPCId": "vpc-8yhq1v63"
                },
                "Status": "RUNNING",
                "Type": "KUBERNETES"
            }
        ],
        "RequestId": "1bc7ec7d-5fa9-42af-ac6d-1ef56f3bf625",
        "TotalCount": 10
    }
}
```

