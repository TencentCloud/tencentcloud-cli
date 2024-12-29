**Example 1: 查询治理中心服务列表**



Input: 

```
tccli tse DescribeGovernanceServices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Name": "name",
                "Namespace": "namespace",
                "Metadatas": [
                    {
                        "Key": "key",
                        "Value": "value"
                    }
                ],
                "Comment": "comment",
                "CreateTime": "2024-10-08 10:00:00",
                "ModifyTime": "2024-10-08 10:00:00",
                "Department": "dev",
                "Business": "web",
                "HealthyInstanceCount": 1,
                "TotalInstanceCount": 1,
                "Id": "id",
                "Editable": true,
                "UserIds": [
                    "101"
                ],
                "GroupIds": [
                    "groupa"
                ],
                "RemoveUserIds": [
                    "12345678"
                ],
                "RemoveGroupIds": [
                    "101"
                ],
                "ExportTo": [
                    "json"
                ]
            }
        ],
        "RequestId": "req-id"
    }
}
```

