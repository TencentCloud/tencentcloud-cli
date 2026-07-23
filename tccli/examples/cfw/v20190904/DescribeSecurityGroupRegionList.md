**Example 1: 查询企业安全组地域列表**



Input: 

```
tccli cfw DescribeSecurityGroupRegionList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Region": "ap-guangzhou",
                "RegionId": "1",
                "RegionName": ""
            }
        ],
        "Total": 27,
        "RequestId": "d7f60666-6f42-4e88-8cf0-7b17635423e1"
    }
}
```

