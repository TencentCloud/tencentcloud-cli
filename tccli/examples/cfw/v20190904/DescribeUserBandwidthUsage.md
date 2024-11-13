**Example 1: 实例1 查询用户带宽流量使用情况**

查询用户带宽流量使用情况

Input: 

```
tccli cfw DescribeUserBandwidthUsage --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "FwEnginType": "NAT防火墙实例",
                "InstanceId": "cfwnat-ef74fdaf",
                "InstanceName": "[autotest][勿删]自动化测试",
                "Percent": 82.19,
                "Quota": 40,
                "Region": "ap-shanghai",
                "RegionName": "上海",
                "UsedWidth": 32.88
            }
        ],
        "RequestId": "535eed3d-4c1e-417a-b1f1-4ee1c6f796e0"
    }
}
```

