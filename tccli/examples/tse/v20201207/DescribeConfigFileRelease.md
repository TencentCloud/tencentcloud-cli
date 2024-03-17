**Example 1: 查询配置文件发布详情**

查询配置文件发布详情

Input: 

```
tccli tse DescribeConfigFileRelease --cli-unfold-argument  \
    --InstanceId ins-fd191a86 \
    --Namespace Polaris \
    --Group group-test-jayhjxu \
    --Name config-file-test
```

Output: 
```
{
    "Response": {
        "ConfigFileRelease": {
            "Id": 1,
            "Name": "abc",
            "Namespace": "abc",
            "Group": "abc",
            "FileName": "abc",
            "Content": "abc",
            "Comment": "abc",
            "Md5": "abc",
            "Version": 1,
            "CreateTime": "abc",
            "CreateBy": "abc",
            "ModifyTime": "abc",
            "ModifyBy": "abc",
            "ReleaseDescription": "abc",
            "Active": true,
            "Format": "abc"
        },
        "RequestId": "abc"
    }
}
```

