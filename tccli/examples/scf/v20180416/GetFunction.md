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
        "ModTime": "2020-09-22 00:00:00",
        "CodeInfo": "abc",
        "Description": "abc",
        "Triggers": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "Type": "abc",
                "TriggerDesc": "abc",
                "TriggerName": "abc",
                "AddTime": "2020-09-22 00:00:00",
                "Enable": 0,
                "CustomArgument": "abc",
                "AvailableStatus": "abc",
                "ResourceId": "abc",
                "BindStatus": "abc",
                "TriggerAttribute": "abc",
                "Qualifier": "abc",
                "Description": "abc"
            }
        ],
        "Handler": "abc",
        "CodeSize": 0,
        "Timeout": 0,
        "FunctionVersion": "abc",
        "MemorySize": 0,
        "Runtime": "abc",
        "FunctionName": "abc",
        "VpcConfig": {
            "VpcId": "abc",
            "SubnetId": "abc"
        },
        "UseGpu": "abc",
        "Environment": {
            "Variables": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ]
        },
        "CodeResult": "abc",
        "CodeError": "abc",
        "ErrNo": 0,
        "Namespace": "abc",
        "Role": "abc",
        "InstallDependency": "abc",
        "Status": "abc",
        "StatusDesc": "abc",
        "ClsLogsetId": "abc",
        "ClsTopicId": "abc",
        "FunctionId": "abc",
        "Tags": [
            {
                "Key": "abc",
                "Value": "abc"
            }
        ],
        "EipConfig": {
            "EipFixed": "abc",
            "Eips": [
                "abc"
            ]
        },
        "AccessInfo": {
            "Host": "abc",
            "Vip": "abc"
        },
        "Type": "abc",
        "L5Enable": "abc",
        "Layers": [
            {
                "CompatibleRuntimes": [
                    "abc"
                ],
                "AddTime": "abc",
                "Description": "abc",
                "LicenseInfo": "abc",
                "LayerVersion": 0,
                "LayerName": "abc",
                "Status": "abc",
                "Stamp": "abc"
            }
        ],
        "DeadLetterConfig": {
            "Type": "abc",
            "Name": "abc",
            "FilterType": "abc"
        },
        "AddTime": "2020-09-22 00:00:00",
        "PublicNetConfig": {
            "PublicNetStatus": "abc",
            "EipConfig": {
                "EipStatus": "abc",
                "EipAddress": [
                    "abc"
                ]
            }
        },
        "OnsEnable": "abc",
        "CfsConfig": {
            "CfsInsList": [
                {
                    "UserId": "abc",
                    "UserGroupId": "abc",
                    "CfsId": "abc",
                    "MountInsId": "abc",
                    "LocalMountDir": "abc",
                    "RemoteMountDir": "abc",
                    "IpAddress": "abc",
                    "MountVpcId": "abc",
                    "MountSubnetId": "abc"
                }
            ]
        },
        "AvailableStatus": "abc",
        "Qualifier": "abc",
        "InitTimeout": 0,
        "StatusReasons": [
            {
                "ErrorCode": "abc",
                "ErrorMessage": "abc"
            }
        ],
        "AsyncRunEnable": "abc",
        "TraceEnable": "abc",
        "ImageConfig": {
            "RegistryId": "abc",
            "ImageType": "abc",
            "ImageUri": "abc",
            "EntryPoint": "abc",
            "Command": "abc",
            "Args": "abc",
            "ContainerImageAccelerate": true,
            "ImagePort": 0
        },
        "ProtocolType": "abc",
        "ProtocolParams": {
            "WSParams": {
                "IdleTimeOut": 1
            }
        },
        "DnsCache": "abc",
        "IntranetConfig": {
            "IpFixed": "abc",
            "IpAddress": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

