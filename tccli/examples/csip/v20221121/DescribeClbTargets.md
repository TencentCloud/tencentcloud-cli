**Example 1: 查询CLB后端服务列表**



Input: 

```
tccli csip DescribeClbTargets --cli-unfold-argument  \
    --AssetID l***mtk*rk*0 \
    --TargetType listener \
    --MemberId mem-68b8*87a6**6**00
```

Output: 
```
{
    "Response": {
        "Targets": [
            {
                "EniID": "eni-0*k*u*v3",
                "InstanceID": "eks-**k*1exe",
                "InstanceName": "",
                "Port": 30438,
                "PrivateIpAddresses": "10*11*.1*1.28"
            }
        ],
        "RequestId": "22565228-80c1-4e30-8768-0cec04d998f2"
    }
}
```

