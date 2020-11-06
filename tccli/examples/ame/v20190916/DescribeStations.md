**Example 1: 获取分类内容（Station）列表**



Input: 

```
tccli ame DescribeStations --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "HaveMore": 0,
        "Offset": 0,
        "RequestId": "s1568780320026098000",
        "Size": 3,
        "Stations": [
            {
                "CategoryCode": "",
                "CategoryID": "DB5C207AE09E058C",
                "ImagePathMap": [
                    {
                        "Key": "JPG-320X320-STATION",
                        "Value": ""
                    },
                    {
                        "Key": "JPG-600X600-STATION",
                        "Value": ""
                    },
                    {
                        "Key": "JPG-NXN-STATION",
                        "Value": ""
                    }
                ],
                "Name": "素材-国风",
                "Rank": 1
            }
        ],
        "Total": 3
    }
}
```

