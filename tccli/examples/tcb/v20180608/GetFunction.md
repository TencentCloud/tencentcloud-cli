**Example 1: GetFunction-0819**



Input: 

```
tccli tcb GetFunction --cli-unfold-argument  \
    --EnvId jackvyli-d1g5v7p5e7191af47 \
    --FunctionName jackvylitest7 \
    --Namespace jackvyli-d1g5v7p5e7191af47
```

Output: 
```
{
    "Response": {
        "AddTime": "2026-08-20 10:53:26",
        "AsyncRunEnable": "FALSE",
        "AvailableStatus": "Available",
        "CodeInfo": "",
        "CodeResult": "success",
        "CodeSize": 0,
        "Description": "Hello World",
        "ErrNo": 0,
        "FunctionId": "lam-bl4u8z57",
        "FunctionName": "jackvylitest7",
        "FunctionVersion": "$LATEST",
        "Handler": "",
        "ImageConfig": {
            "Args": "",
            "Command": "",
            "ContainerImageAccelerate": false,
            "ImageType": "",
            "ImageUri": "",
            "RegistryId": ""
        },
        "InitTimeout": 65,
        "InstallDependency": "TRUE",
        "L5Enable": "FALSE",
        "MemorySize": 256,
        "ModTime": "2026-08-20 10:53:26",
        "Namespace": "jackvyli-d1g5v7p5e7191af47",
        "OnsEnable": "FALSE",
        "Qualifier": "$LATEST",
        "RequestId": "94070739-c916-496b-9e2a-3f93cf69fc9d",
        "Role": "TCB_QcsRole",
        "Runtime": "Nodejs18.15",
        "Status": "Creating",
        "Tags": [],
        "Timeout": 3,
        "TraceEnable": "FALSE",
        "Triggers": [],
        "Type": "HTTP",
        "UseGpu": "FALSE",
        "VpcConfig": {
            "SubnetId": "subnet-2tvkenrt",
            "VpcId": "vpc-3m4f4bhq"
        }
    }
}
```

