**Example 1: 查询Bot数量**



Input: 

```
tccli waf DescribeHistogram --cli-unfold-argument  \
    --FromTime 2024-11-03 00:00:00 \
    --ToTime 2024-11-03 15:17:00 \
    --Host all \
    --Source access \
    --QueryField ip
```

Output: 
```
{
    "Response": {
        "Histogram": [
            "{\"count\":43,\"ip\":\"128.14.129.10\"}",
            "{\"count\":43,\"ip\":\"8.220.210.24\"}",
            "{\"count\":42,\"ip\":\"185.191.126.248\"}",
            "{\"count\":40,\"ip\":\"141.98.11.178\"}",
            "{\"count\":33,\"ip\":\"9.190.110.251\"}"
        ],
        "RequestId": "cce2cdd7-8e54-4c08-b669-648adb1b49c1"
    }
}
```

