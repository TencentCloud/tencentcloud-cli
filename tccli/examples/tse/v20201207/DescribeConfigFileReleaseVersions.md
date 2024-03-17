**Example 1: 获取配置版本列表**

获取配置版本列表

Input: 

```
tccli tse DescribeConfigFileReleaseVersions --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace abc \
    --Group abc \
    --FileName abc
```

Output: 
```
{
    "Response": {
        "ReleaseVersions": [
            {
                "Name": "abc",
                "Active": true
            }
        ],
        "RequestId": "abc"
    }
}
```

