**Example 1: 获取用户可用的地域列表**

获取用户可用的地域列表

Input: 

```
tccli tccatalog DescribeRegionWhitelist --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AvailableRegion": [
            {
                "Group": "华北地区",
                "Name": "北京",
                "RegionId": 8,
                "RegionApCode": "ap-beijing"
            }
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

