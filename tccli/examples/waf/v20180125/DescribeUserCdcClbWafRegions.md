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
                        "Name": "xxx"
                    },
                    {
                        "Id": "cluster-o41khj99",
                        "Name": "xxx"
                    }
                ]
            }
        ],
        "RequestId": "123456789"
    }
}
```

