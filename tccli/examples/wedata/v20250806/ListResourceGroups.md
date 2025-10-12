**Example 1: 查询调度资源组**



Input: 

```
tccli wedata ListResourceGroups --cli-unfold-argument  \
    --Type Schedule \
    --Name None \
    --ProjectIds None \
    --PageNumber None \
    --PageSize None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssociateProjects": [
                        {
                            "ProjectDisplayName": "数据探索_notebook验证",
                            "ProjectId": "2153380290671734784",
                            "ProjectName": null
                        }
                    ],
                    "Description": "开发调度资源组-notebook专用",
                    "Id": "20240401132517098618",
                    "Name": "sche_group_notebook_1",
                    "Region": "上海",
                    "ResourceGroupType": "Schedule",
                    "SubNet": "subnet-ecs42j4h",
                    "VpcId": "vpc-s1p37c5i"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "ed5d6286-ce77-487b-91c7-bfd4285375a4"
    }
}
```

