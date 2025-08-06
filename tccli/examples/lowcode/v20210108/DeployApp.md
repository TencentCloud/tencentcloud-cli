**Example 1: 发布应用**



Input: 

```
tccli lowcode DeployApp --cli-unfold-argument  \
    --BuildType web \
    --Id app-k82WCM8 \
    --Mode upload \
    --EnvId lowcode-5gzbnlv393348d \
    --SubAppIds sub-7x2cST
```

Output: 
```
{
    "Response": {
        "BuildId": "bcad608f-962b-c1c6f403d6e1",
        "DeployErrCode": 0,
        "DeployErrMsg": "",
        "RequestId": "1cfaee37-93e8c08c47d"
    }
}
```

