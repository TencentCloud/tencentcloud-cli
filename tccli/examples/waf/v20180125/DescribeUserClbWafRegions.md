**Example 1: 获取对客户已经开放的负载均衡型WAF的地域**



Input: 

```
tccli waf DescribeUserClbWafRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            "ap-guangzhou",
            "ap-shanghai"
        ],
        "RequestId": "4c8827fc-839c-4ecc-8ac5-d39456d163b9"
    }
}
```

