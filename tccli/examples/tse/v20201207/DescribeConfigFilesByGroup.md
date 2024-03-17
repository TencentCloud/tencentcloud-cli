**Example 1: DescribeConfigFilesByGroup 示例**

根据 group 与 namespace 查询 配置文件

Input: 

```
tccli tse DescribeConfigFilesByGroup --cli-unfold-argument  \
    --InstanceId ins-fd191a86 \
    --Namespace Polaris \
    --Group group-test-jayhjxu
```

Output: 
```
{
    "Response": {
        "ConfigFiles": [
            {
                "Id": 6,
                "Name": "test-for_create_file",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "Content": "",
                "Format": "text",
                "Comment": "dsgasdgas",
                "Status": "to-be-released",
                "Tags": [
                    {
                        "Key": "key2",
                        "Value": "value1"
                    },
                    {
                        "Key": "key1",
                        "Value": "value2"
                    }
                ],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": "",
                "ReleaseTime": "",
                "ReleaseBy": ""
            },
            {
                "Id": 4,
                "Name": "config-file-test",
                "Namespace": "Polaris",
                "Group": "group-test-jayhjxu",
                "Content": "test for ModifyConfigFiles",
                "Format": "text",
                "Comment": "ModifyConfigFiles comment after modified",
                "Status": "success",
                "Tags": [],
                "CreateTime": "",
                "CreateBy": "",
                "ModifyTime": "",
                "ModifyBy": "",
                "ReleaseTime": "",
                "ReleaseBy": ""
            }
        ],
        "RequestId": "jayhjxu-test-DescribeConfigFilesByGroup--ssss",
        "TotalCount": 2
    }
}
```

