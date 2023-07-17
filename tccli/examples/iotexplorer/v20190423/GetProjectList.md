**Example 1: 查询项目列表**

当用户在自己的业务系统中想进行产品管理时，可以通过查询项目列表接口查询用户在物联网开发平台创建的项目。

Input: 

```
tccli iotexplorer GetProjectList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Projects": [
            {
                "ProjectId": "prj-***2v",
                "ProjectName": "name",
                "ProjectDesc": "",
                "CreateTime": 1657334314,
                "UpdateTime": 1685669118,
                "ProductCount": 1,
                "ApplicationCount": 1,
                "DeviceCount": 2,
                "NativeAppCount": 0,
                "WebAppCount": 0,
                "InstanceId": "ins-V**A",
                "EnableOpenState": 1
            }
        ],
        "Total": 1,
        "RequestId": "8525aa8d-6820-4977-b64c-1f3370919a9e"
    }
}
```

