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
        "ModTime": "2018-06-07 09:52:23",
        "Environment": {
            "Variables": []
        },
        "CodeError": "",
        "Description": "",
        "VpcConfig": {
            "SubnetId": "",
            "VpcId": ""
        },
        "Triggers": [],
        "ErrNo": 0,
        "UseGpu": "FALSE",
        "CodeSize": 0,
        "MemorySize": 128,
        "Namespace": "default",
        "FunctionVersion": "$LATEST",
        "Timeout": 3,
        "RequestId": "a1ffbba5-5489-45bc-89c5-453e50d5386e",
        "CodeResult": "failed",
        "Handler": "scfredis.main_handler",
        "Runtime": "Python2.7",
        "FunctionName": "ledDummyAPITest",
        "CodeInfo": "",
        "Role": "",
        "Qualifier": "$LATEST",
        "AvailableStatus": "Available",
        "CfsConfig": {
            "CfsInsList": [
                {
                    "LocalMountDir": "",
                    "RemoteMountDir": "",
                    "MountInsId": "",
                    "UserId": 0,
                    "UserGroupId": 0,
                    "CfsId": "",
                    "IpAddress": "",
                    "MountVpcId": "",
                    "MountSubnetId": ""
                }
            ]
        }
    }
}
```

