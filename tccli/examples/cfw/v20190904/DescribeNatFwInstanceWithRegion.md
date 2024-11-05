**Example 1: GetNatInstance 获取租户所有NAT实例**



Input: 

```
tccli cfw DescribeNatFwInstanceWithRegion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NatinsLst": [
            {
                "NatinsId": "cfwnat-fc7ae792",
                "NatinsName": "运维测试",
                "Region": "ap-guangzhou",
                "FwMode": 1,
                "Status": 0,
                "NatIp": "1.1.1.1,2.2.2.2"
            }
        ],
        "RequestId": "52fa6827-985f-49c7-a853-d86efbd547c3"
    }
}
```

