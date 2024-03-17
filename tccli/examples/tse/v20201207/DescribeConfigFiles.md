**Example 1: 查询配置文件列表**

根据命名空间、组名与文件名查询

Input: 

```
tccli tse DescribeConfigFiles --cli-unfold-argument  \
    --InstanceId ins-d734da06 \
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
        "ConfigFiles": [
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
        "RequestId": "jayhjxu-DescribeConfigFiles-test-1024",
        "TotalCount": 1
    }
}
```

