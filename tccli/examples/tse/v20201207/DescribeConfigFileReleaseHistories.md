**Example 1: 查询配置文件发布历史记录-不指定EndId**

查询配置文件发布历史记录-不指定EndId

Input: 

```
tccli tse DescribeConfigFileReleaseHistories --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace Polaris \
    --Group group-test-jayhjxu \
    --Name config-file-test \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ConfigFileReleaseHistories": [
            {
                "Id": 5,
                "Name": "config-file-test",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "FileName": "",
                "Content": "test for ModifyConfigFiles",
                "Format": "text",
                "Comment": "",
                "Md5": "9dafe0dd6604b83bb2a40cae654872fa",
                "Type": "normal",
                "Status": "success",
                "Tags": [],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": ""
            },
            {
                "Id": 4,
                "Name": "ConfigFileReleases test",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "FileName": "",
                "Content": "test for CreateConfigFile",
                "Format": "text",
                "Comment": "test for 1",
                "Md5": "4df12e4b1cd8d029a5a233596869fc66",
                "Type": "normal",
                "Status": "success",
                "Tags": [],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": ""
            },
            {
                "Id": 3,
                "Name": "ConfigFileReleases test",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "FileName": "",
                "Content": "",
                "Format": "text",
                "Comment": "",
                "Md5": "",
                "Type": "delete",
                "Status": "success",
                "Tags": [],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": ""
            },
            {
                "Id": 2,
                "Name": "ConfigFileReleases test",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "FileName": "",
                "Content": "test for CreateConfigFile",
                "Format": "text",
                "Comment": "test for 1",
                "Md5": "4df12e4b1cd8d029a5a233596869fc66",
                "Type": "normal",
                "Status": "success",
                "Tags": [],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": ""
            }
        ],
        "RequestId": "jayhjxu-test-DescribeConfigFileRelease--ssss",
        "TotalCount": 4
    }
}
```

**Example 2: 指定EndId用于优化分页-指定EndId用于优化分页**

指定EndId用于优化分页-指定EndId用于优化分页

Input: 

```
tccli tse DescribeConfigFileReleaseHistories --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace abc \
    --Group abc \
    --Name abc \
    --EndId 3 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "ConfigFileReleaseHistories": [
            {
                "Id": 2,
                "Name": "ConfigFileReleases test",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "FileName": "",
                "Content": "test for CreateConfigFile",
                "Format": "text",
                "Comment": "test for 1",
                "Md5": "4df12e4b1cd8d029a5a233596869fc66",
                "Type": "normal",
                "Status": "success",
                "Tags": [],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": ""
            }
        ],
        "RequestId": "jayhjxu-test-DescribeConfigFileRelease--ssss",
        "TotalCount": 1
    }
}
```

