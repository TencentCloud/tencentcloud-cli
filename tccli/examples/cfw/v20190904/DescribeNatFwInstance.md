**Example 1: DescribeNatFwInstance 获取租户所有NAT实例**



Input: 

```
tccli cfw DescribeNatFwInstance --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NatinsLst": [
            {
                "NatinsId": "cfwnat-9243de20",
                "NatinsName": "公网NAT出口",
                "Region": "ap-shanghai",
                "FwMode": 0,
                "Status": 0,
                "NatIp": "1.1.1.1,2.2.2.2"
            }
        ],
        "RequestId": "9a86c4e3-b926-4244-919b-aba9a7e82686"
    }
}
```

