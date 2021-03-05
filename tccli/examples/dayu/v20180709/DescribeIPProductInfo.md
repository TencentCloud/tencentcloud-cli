**Example 1: 获取独享包或共享包IP对应的云资产信息**



Input: 

```
tccli dayu DescribeIPProductInfo --cli-unfold-argument  \
    --Business bgp \
    --IpList 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "8466d9e1-70a9-4575-8e02-df15bd50bc49"
    }
}
```

