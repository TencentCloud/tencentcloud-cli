**Example 1: 查询集群模式Vpc间防火墙开关**

查询集群模式Vpc间防火墙开关

Input: 

```
tccli cfw DescribeClusterVpcFwSwitchs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetType": "ccn",
                "AttachIns": [
                    {
                        "InsId": "vpc-eohwqlql",
                        "InsName": "cfwtest2"
                    }
                ],
                "Endpoints": null,
                "FwType": "ew",
                "Idpsaction": 0,
                "InsObj": "ccn-ha7tt32f",
                "IpVersion": 0,
                "NonCluster": 0,
                "ObjName": "ccn-test",
                "Region": "",
                "RoutingMode": 0,
                "Status": 0,
                "SwitchMode": 2,
                "TransEnable": 0
            }
        ],
        "Total": 1,
        "RequestId": "291bae45-ec59-423a-a544-968d6c00b9a2"
    }
}
```

