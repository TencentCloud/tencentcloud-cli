**Example 1: Getting function details**

This example shows you how to get the information of the corresponding function. You can specify the version and namespace.

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

