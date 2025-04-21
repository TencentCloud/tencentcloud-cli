**Example 1: 检查业务资源导入任务结果**

检查业务资源导入任务结果

Input: 

```
tccli ioa DescribeCheckBusinessResourcesResult --cli-unfold-argument  \
    --TaskID abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "GroupName": "abc",
                    "ResourceName": "abc",
                    "ResourceType": "abc",
                    "ResourceAddr": "abc",
                    "ResourcePorts": "abc",
                    "DirectConn": "abc",
                    "Protocol": "abc",
                    "PrivateNetName": "abc",
                    "Errors": [
                        {
                            "Field": "abc",
                            "ErrorMsg": "abc"
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

