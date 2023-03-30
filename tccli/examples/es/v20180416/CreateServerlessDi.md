**Example 1: 创建cvm数据接入**

创建cvm数据接入

Input: 

```
tccli es CreateServerlessDi --cli-unfold-argument  \
    --DiSourceType cvm \
    --DiSourceCvm.VpcId vpc-xxx \
    --DiSourceCvm.CvmIds ins-xxx \
    --DiSourceCvm.LogPaths /data \
    --DiSourceTke.VpcId vpc-xxx \
    --DiSourceTke.TkeId tke-xxx \
    --DiSinkServerless.ServerlessId sid-xxx
```

Output: 
```
{
    "Response": {
        "DiId": "sid-xxx",
        "RequestId": "xxx-xxx-xxx"
    }
}
```

