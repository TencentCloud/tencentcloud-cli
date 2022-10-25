**Example 1: 查询可加速域名**

查询可加速域名

Input: 

```
tccli vpc DescribeOverseaAcceleratorRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "ShortName": "gz",
                "Name": "广州",
                "IsChinaMainland": true,
                "IsFinance": false,
                "WhiteListKey": [],
                "AvailableZoneSet": []
            },
            {
                "Region": "ap-shanghai",
                "RegionId": 4,
                "ShortName": "sh",
                "Name": "上海",
                "IsChinaMainland": true,
                "IsFinance": false,
                "WhiteListKey": [],
                "AvailableZoneSet": []
            }
        ],
        "TotalCount": 2,
        "RequestId": "253b82ae-764f-48f4-8301-02a52ae29fe4"
    }
}
```

