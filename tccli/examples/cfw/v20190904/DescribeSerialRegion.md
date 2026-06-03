**Example 1: 查询串行防火墙地域带宽分配信息**

查询串行防火墙地域带宽分配信息

Input: 

```
tccli cfw DescribeSerialRegion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SerialRegionLst": [
            {
                "Region": "ap-shanghai",
                "Width": 100
            }
        ],
        "UnUsedWidth": 100,
        "UnUsedQuota": 100,
        "RequestId": "11122333313"
    }
}
```

