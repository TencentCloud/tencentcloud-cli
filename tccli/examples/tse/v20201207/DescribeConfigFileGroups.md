**Example 1: 查询配置文件组列表**

根据条件查询配置文件组列表

Input: 

```
tccli tse DescribeConfigFileGroups --cli-unfold-argument  \
    --InstanceId janice-test \
    --Limit 1 \
    --Namespace namespace_test \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 125,
        "ConfigFileGroups": [
            {
                "Id": 1,
                "Name": "configFileGroupName",
                "Namespace": "namespace1",
                "Comment": "test config",
                "CreateTime": "2023-03-08 00:00:00",
                "CreateBy": "jayhjxu",
                "ModifyTime": "2023-03-08 12:00:00",
                "ModifyBy": "jayhjxu",
                "FileCount": 1,
                "UserIds": [
                    "user_1"
                ],
                "GroupIds": [
                    "group_1"
                ],
                "RemoveUserIds": [
                    "user_2"
                ],
                "RemoveGroupIds": [
                    "group_2"
                ],
                "Editable": true,
                "Owner": "jayhjxu"
            }
        ],
        "RequestId": "63d46143-c731-4aff-b0c9-edce7401db32"
    }
}
```

