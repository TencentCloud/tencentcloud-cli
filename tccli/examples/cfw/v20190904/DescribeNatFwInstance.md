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
                "NatinsName": "ywold",
                "Region": "ap-shanghai",
                "FwMode": 0,
                "Status": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

