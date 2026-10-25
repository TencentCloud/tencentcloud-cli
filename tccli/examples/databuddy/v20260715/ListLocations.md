**Example 1: 查询存储位置列表**

分页查询存储位置列表

Input: 

```
tccli databuddy ListLocations --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Locations": [
                {
                    "Audit": {
                        "CreatedAt": "1776757339732",
                        "Creator": "********4619",
                        "CreatorName": "*******0**e******n*e**.***",
                        "LastModifiedAt": "1777380384696",
                        "LastModifier": "********4619",
                        "LastModifierName": "********-t****@*e*****.com"
                    },
                    "Comment": "编辑描述123123123",
                    "LocationName": "bucunzaibucunzai",
                    "LocationUri": "***://*ta*n*ti**c**y*******************p***a**z**u********9*",
                    "Properties": []
                }
            ],
            "SnapshotId": "",
            "TotalCount": 11
        },
        "RequestId": "e9bf167d-c38f-4de4-a6eb-0c7e19bdc0ff"
    }
}
```

