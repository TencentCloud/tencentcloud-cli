**Example 1: 查询项目详情**

查询项目详情

Input: 

```
tccli iotexplorer DescribeProject --cli-unfold-argument  \
    --ProjectId prj-4r2kajtp
```

Output: 
```
{
    "Response": {
        "Project": {
            "ProjectId": "prj-***6sm",
            "ProjectName": "leo",
            "ProjectDesc": "",
            "CreateTime": 1626080984,
            "UpdateTime": 1626080984,
            "ProductCount": 1,
            "ApplicationCount": 0,
            "DeviceCount": 0,
            "NativeAppCount": 0,
            "WebAppCount": 0,
            "InstanceId": "ins-DG**F7",
            "EnableOpenState": 0
        },
        "RequestId": "a5170c4f-4cf7-4648-8c74-cae58ca3b048"
    }
}
```

