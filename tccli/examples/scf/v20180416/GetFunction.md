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
        "Layers": [
            {
                "Status": "xx",
                "LayerVersion": 0,
                "Description": "xx",
                "LicenseInfo": "xx",
                "AddTime": "xx",
                "CompatibleRuntimes": [
                    "xx"
                ],
                "LayerName": "xx"
            }
        ],
        "CodeError": "xx",
        "AccessInfo": {
            "Host": "xx",
            "Vip": "xx"
        },
        "UseGpu": "xx",
        "EipConfig": {
            "EipFixed": "xx",
            "Eips": [
                "xx"
            ]
        },
        "Namespace": "xx",
        "Environment": {
            "Variables": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ]
        },
        "OnsEnable": "xx",
        "InstallDependency": "xx",
        "Role": "xx",
        "StatusReasons": [
            {
                "ErrorCode": "xx",
                "ErrorMessage": "xx"
            }
        ],
        "Description": "xx",
        "Type": "xx",
        "Status": "xx",
        "Runtime": "xx",
        "DeadLetterConfig": {
            "FilterType": "xx",
            "Type": "xx",
            "Name": "xx"
        },
        "Qualifier": "xx",
        "Tags": [
            {
                "Value": "xx",
                "Key": "xx"
            }
        ],
        "ClsLogsetId": "xx",
        "FunctionId": "xx",
        "FunctionVersion": "xx",
        "FunctionName": "xx",
        "Triggers": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "BindStatus": "xx",
                "Enable": 0,
                "TriggerAttribute": "xx",
                "Qualifier": "xx",
                "CustomArgument": "xx",
                "AddTime": "2020-09-22 00:00:00",
                "AvailableStatus": "xx",
                "TriggerDesc": "xx",
                "TriggerName": "xx",
                "ResourceId": "xx",
                "Type": "xx"
            }
        ],
        "ClsTopicId": "xx",
        "AddTime": "2020-09-22 00:00:00",
        "MemorySize": 128,
        "CfsConfig": {
            "CfsInsList": [
                {
                    "MountSubnetId": "xx",
                    "LocalMountDir": "xx",
                    "UserId": "xx",
                    "IpAddress": "xx",
                    "MountInsId": "xx",
                    "MountVpcId": "xx",
                    "UserGroupId": "xx",
                    "CfsId": "xx",
                    "RemoteMountDir": "xx"
                }
            ]
        },
        "Timeout": 3,
        "StatusDesc": "xx",
        "CodeInfo": "xx",
        "VpcConfig": {
            "SubnetId": "xx",
            "VpcId": "xx"
        },
        "ErrNo": 0,
        "CodeSize": 0,
        "L5Enable": "xx",
        "AvailableStatus": "xx",
        "Handler": "xx",
        "CodeResult": "xx",
        "PublicNetConfig": {
            "EipConfig": {
                "EipAddress": [
                    "xx"
                ],
                "EipStatus": "xx"
            },
            "PublicNetStatus": "xx"
        },
        "InitTimeout": 0,
        "RequestId": "xx"
    }
}
```

