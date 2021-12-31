**Example 1: 查询实例文件包列表**

查询实例文件包列表

Input: 

```
tccli es DescribeInstanceBundleList --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BundleList": [
            {
                "BundleName": "my_dict",
                "TargetPath": "/config",
                "Status": 1
            }
        ],
        "RequestId": "42c690ef-ad47-4dd4-8427-7eb618c3177d"
    }
}
```

