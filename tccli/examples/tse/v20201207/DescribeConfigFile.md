**Example 1: 查询单个配置文件详细**

查询单个配置文件详细

Input: 

```
tccli tse DescribeConfigFile --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace abc \
    --Group abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "ConfigFile": {
            "Id": 1,
            "Name": "abc",
            "Namespace": "abc",
            "Group": "abc",
            "Content": "abc",
            "Format": "abc",
            "Comment": "abc",
            "Status": "abc",
            "Tags": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "CreateTime": "abc",
            "CreateBy": "abc",
            "ModifyTime": "abc",
            "ModifyBy": "abc",
            "ReleaseTime": "abc",
            "ReleaseBy": "abc"
        },
        "RequestId": "abc"
    }
}
```

