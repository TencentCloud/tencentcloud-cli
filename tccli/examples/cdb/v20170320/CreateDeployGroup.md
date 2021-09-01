**Example 1: 创建置放群组**

用户可以通过该接口创建置放群组

Input: 

```
tccli cdb CreateDeployGroup --cli-unfold-argument  \
    --DeployGroupName cdb-ezq1vzem \
    --Description test
```

Output: 
```
{
    "Response": {
        "DeployGroupId": "213123",
        "RequestId": "b4a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

