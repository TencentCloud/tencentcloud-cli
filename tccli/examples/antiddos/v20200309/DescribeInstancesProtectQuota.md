**Example 1: 查询资产防护规格**



Input: 

```
tccli antiddos DescribeInstancesProtectQuota --cli-unfold-argument  \
    --InstanceInfos.0.InstanceId abc \
    --InstanceInfos.0.IpList 1.1.1.1 2.2.2.2 \
    --DevType lighthouse
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "Specifications": [
            {
                "InstanceId": "lhins-xxxx",
                "Business": "basic",
                "DDoSMax": 100,
                "Status": "normal",
                "Quota": 999999
            },
            {
                "InstanceId": "lhins-xxxx",
                "Business": "basic",
                "DDoSMax": 100,
                "Status": "normal",
                "Quota": 999999
            }
        ]
    }
}
```

