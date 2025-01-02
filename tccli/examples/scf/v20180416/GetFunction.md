**Example 1: 获取函数详细信息**

用户用此函数获取对应的函数信息，可指定版本与命名空间。

Input: 

```
tccli scf GetFunction --cli-unfold-argument  \
    --FunctionName <FunctionName>
```

Output: 
```
{
    "Response": {
        "Qualifier": "$LATEST",
        "Description": "Created by Serverless",
        "Timeout": 3,
        "InitTimeout": 90,
        "MemorySize": 128,
        "Runtime": "CustomImage",
        "VpcConfig": {
            "VpcId": "",
            "SubnetId": ""
        },
        "Environment": {
            "Variables": []
        },
        "Handler": "",
        "UseGpu": "FALSE",
        "Role": "",
        "CodeSize": 0,
        "FunctionVersion": "$LATEST",
        "FunctionName": "function-index1",
        "FunctionId": "xccxvxcv",
        "Namespace": "default",
        "InstallDependency": "FALSE",
        "Status": "Active",
        "AvailableStatus": "Available",
        "StatusDesc": "",
        "L5Enable": "FALSE",
        "DnsCache": "FALSE",
        "EipConfig": {
            "EipFixed": "FALSE",
            "Eips": []
        },
        "ModTime": "2024-12-17 17:52:48",
        "AddTime": "2024-12-17 17:47:08",
        "Layers": [],
        "DeadLetterConfig": {
            "Type": "",
            "Name": "",
            "FilterType": ""
        },
        "OnsEnable": "FALSE",
        "PublicNetConfig": {
            "PublicNetStatus": "ENABLE",
            "EipConfig": {
                "EipStatus": "DISABLE",
                "EipAddress": []
            }
        },
        "ImageConfig": {
            "RegistryId": "",
            "ImageType": "personal",
            "ImageUri": "ccr.ccs.tencentyun.com/xxx/xxx:xx@sha256:xxxxxxxxxx",
            "ContainerImageAccelerate": false,
            "Command": "node",
            "Args": " index.js ",
            "ImagePort": 9000,
            "EntryPoint": null
        },
        "ProtocolType": "",
        "Triggers": [],
        "ClsLogsetId": "b91e2c12-cccccccccccc",
        "ClsTopicId": "a3b039f5-bbbbbbbbbb",
        "CodeInfo": "",
        "CodeResult": "success",
        "CodeError": "",
        "ErrNo": 0,
        "Tags": [],
        "AccessInfo": {
            "Host": "",
            "Vip": ""
        },
        "Type": "Event",
        "CfsConfig": {
            "CfsInsList": []
        },
        "StatusReasons": [],
        "AsyncRunEnable": "FALSE",
        "TraceEnable": "FALSE",
        "ProtocolParams": null,
        "IntranetConfig": {
            "IpFixed": "DISABLE"
        },
        "RequestId": "08b4c93b-b515-4cf4-a7a3-72b5db4e21dc"
    }
}
```

