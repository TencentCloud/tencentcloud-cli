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
                "NatinsName": "wy yw 测试",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "52fa6827-985f-49c7-a853-d86efbd547c3"
    }
}
```

