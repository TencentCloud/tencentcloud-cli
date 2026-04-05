**Example 1: 创建数据集**



Input: 

```
tccli wedata CreateApplicationDataset --cli-unfold-argument  \
    --DisplayName 无标题数据集3 \
    --WorkspaceId 17663856806379896 \
    --DashboardAccessKey 801469279624839168 \
    --Catalog c4 \
    --Schema default
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatasetVersion": 0,
            "Key": "06d6d98a1769003243305268842bc"
        },
        "RequestId": "cacb8784-addc-4d06-9563-29bd1315a592"
    }
}
```

