**Example 1: 创建cvm数据接入**

创建cvm数据接入

Input: 

```
tccli es CreateServerlessDi --cli-unfold-argument  \
    --DiSourceType xx \
    --DiSourceCvm.VpcId xx \
    --DiSourceCvm.CvmIds xx \
    --DiSourceCvm.LogPaths xx \
    --DiSourceTke.VpcId xx \
    --DiSourceTke.TkeId xx \
    --DiSinkServerless.ServerlessId xx
```

Output: 
```
{
    "Response": {
        "DiId": "xx",
        "RequestId": "xx"
    }
}
```

