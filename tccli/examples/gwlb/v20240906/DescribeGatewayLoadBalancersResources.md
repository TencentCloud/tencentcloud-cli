**Example 1: 查询部署了GWLB集群的可用区**

查询部署了GWLB集群的可用区

Input: 

```
tccli gwlb DescribeGatewayLoadBalancersResources --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "33a90f66-209e-4554-948a-c9652c08776e",
        "TotalCount": 1,
        "ZoneResourceSet": [
            {
                "MasterZone": "ap-guangzhou-2"
            }
        ]
    }
}
```

