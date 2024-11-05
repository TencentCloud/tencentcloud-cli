**Example 1: 获取CDC场景下对客户已经开放的负载均衡型WAF的地域**



Input: 

```
tccli waf DescribeUserCdcClbWafRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Region": "gz",
                "Clusters": [
                    {
                        "Id": "cluster-o41khj88",
                        "Name": "cltregiona"
                    },
                    {
                        "Id": "cluster-o41khj99",
                        "Name": "cltregionb"
                    }
                ]
            }
        ],
        "RequestId": "2957f686-b290-44ef-a742-b1a169bebae2"
    }
}
```

