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
                "Name": "abc",
                "Namespace": "abc",
                "Metadatas": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Comment": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "Department": "abc",
                "Business": "abc",
                "HealthyInstanceCount": 1,
                "TotalInstanceCount": 1,
                "Id": "abc",
                "Editable": true,
                "UserIds": [
                    "abc"
                ],
                "GroupIds": [
                    "abc"
                ],
                "RemoveUserIds": [
                    "abc"
                ],
                "RemoveGroupIds": [
                    "abc"
                ],
                "ExportTo": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

