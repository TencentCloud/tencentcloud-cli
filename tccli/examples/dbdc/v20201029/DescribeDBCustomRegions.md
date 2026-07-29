**Example 1: 查询 DB Custom 支持的地域列表**



Input: 

```
tccli dbdc DescribeDBCustomRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "Region": "ap-chengdu",
                "RegionState": "SELL"
            }
        ],
        "RequestId": "9d23d840-eade-4f0b-9efb-20e34df7f1dc"
    }
}
```

