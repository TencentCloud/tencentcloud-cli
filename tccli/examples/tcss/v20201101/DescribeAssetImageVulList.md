**Example 1: 查询镜像漏洞列表**



Input: 

```
tccli tcss DescribeAssetImageVulList --cli-unfold-argument  \
    --ImageID csnjkcnshj
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Category": "xx",
                "CVEID": "xx",
                "Tag": [
                    "xx"
                ],
                "Name": "xx",
                "Reference": "xx",
                "Level": 1,
                "FixedVersions": "xx",
                "CVSSV3Score": 10,
                "Des": "xx",
                "Component": "xx",
                "IsSuggest": true,
                "SubmitTime": "xx",
                "Version": "xx",
                "DefenseSolution": "xx",
                "OfficialSolution": "xx",
                "CategoryType": "xx",
                "CVSSV3Desc": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

