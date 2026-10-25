**Example 1: 查询特征表列表**



Input: 

```
tccli databuddy ListFeatureTables --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Items": [
                {
                    "FullName": "my_catalog.my_schema.my_table",
                    "Name": "my_table"
                }
            ],
            "NextPageToken": ""
        }
    }
}
```

