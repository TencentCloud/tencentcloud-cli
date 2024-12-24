**Example 1: 获取配置版本列表**

获取配置版本列表

Input: 

```
tccli tse DescribeConfigFileReleaseVersions --cli-unfold-argument  \
    --InstanceId ins-id \
    --Namespace namespace \
    --Group group \
    --FileName a.yaml
```

Output: 
```
{
    "Response": {
        "ReleaseVersions": [
            {
                "Name": "a.yaml",
                "Active": true
            }
        ],
        "RequestId": "req-id"
    }
}
```

