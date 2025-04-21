**Example 1: 示例1**



Input: 

```
tccli ioa DescribeCommonConfigs --cli-unfold-argument  \
    --Names AccountDeviceBind
```

Output: 
```
{
    "Response": {
        "RequestId": "13a8d60b-6867-4871-b8d1-52447c056f78",
        "Data": {
            "Items": [
                {
                    "Description": "",
                    "Name": "AccountDeviceBind",
                    "CreateTime": "2022-08-29 15:55:02",
                    "Value": "0",
                    "UpdateTime": "2022-10-21 11:02:59",
                    "Id": 1169501
                }
            ]
        }
    }
}
```

**Example 2: 查看安全日志配置**

查看安全日志配置

Input: 

```
tccli ioa DescribeCommonConfigs --cli-unfold-argument  \
    --Names securityCtrlLog
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2024-02-22 20:10:30",
                    "Description": "",
                    "Id": 1184440,
                    "Name": "securityCtrlLog",
                    "UpdateTime": "2024-02-22 20:10:30",
                    "Value": "{\"Enable\":1,\"TimeType\":1,\"CleanDays\":180,\"Day\":1,\"Hour\":0,\"Minute\":0}"
                }
            ]
        },
        "RequestId": "418df94a-769e-44c2-826f-60b6ac8ff600"
    }
}
```

