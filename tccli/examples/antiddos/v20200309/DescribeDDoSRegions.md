**Example 1: 获取高防支持产品地域**



Input: 

```
tccli antiddos DescribeDDoSRegions --cli-unfold-argument  \
    --DevType lighthouse \
    --Edition insurance \
    --International 0
```

Output: 
```
{
    "Response": {
        "Regions": [
            "ap-guangzhou",
            "ap-beijing",
            "ap-shanghai"
        ],
        "RequestId": "abc"
    }
}
```

