**Example 1: 查询负载均衡的操作保护信息**



Input: 

```
tccli clb DescribeLBOperateProtect --cli-unfold-argument  \
    --LoadBalancerIds lb-rbw529fz
```

Output: 
```
{
    "Response": {
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-rbw529fz",
                "ProtectState": true,
                "OperatorUin": "125674504xx",
                "Description": "CLB Operate Protect",
                "ModifyTime": "2021-09-08 15:54:46"
            }
        ],
        "RequestId": "63d7d5d7-523a-4c5e-bda2-ec953ed5ace4"
    }
}
```

