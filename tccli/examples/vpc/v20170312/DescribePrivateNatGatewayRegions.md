**Example 1: 查询私网NAT网关可支持地域**



Input: 

```
tccli vpc DescribePrivateNatGatewayRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "NatProductVersion": 2,
                "RegionId": 19,
                "Region": "ap-chongqing",
                "ShortName": "cq",
                "Name": "重庆",
                "IsChinaMainland": true,
                "IsFinance": false,
                "Area": "西南地区"
            },
            {
                "NatProductVersion": 2,
                "RegionId": 1,
                "Region": "ap-guangzhou",
                "ShortName": "gz",
                "Name": "广州",
                "IsChinaMainland": true,
                "IsFinance": false,
                "Area": "华南地区"
            },
            {
                "NatProductVersion": 2,
                "RegionId": 4,
                "Region": "ap-shanghai",
                "ShortName": "sh",
                "Name": "上海",
                "IsChinaMainland": true,
                "IsFinance": false,
                "Area": "华东地区"
            },
            {
                "NatProductVersion": 2,
                "RegionId": 8,
                "Region": "ap-beijing",
                "ShortName": "bj",
                "Name": "北京",
                "IsChinaMainland": true,
                "IsFinance": false,
                "Area": "华北地区"
            },
            {
                "NatProductVersion": 2,
                "RegionId": 16,
                "Region": "ap-chengdu",
                "ShortName": "cd",
                "Name": "成都",
                "IsChinaMainland": true,
                "IsFinance": false,
                "Area": "西南地区"
            }
        ],
        "TotalCount": 5,
        "RequestId": "5f24dd8e-bb8d-4e32-aba5-31a368745c7e"
    }
}
```

