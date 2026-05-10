**Example 1: 获取 AIGC 高级自定义主体**



Input: 

```
tccli vod DescribeAigcAdvancedCustomElements --cli-unfold-argument  \
    --SubAppId 251007502 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "ElementSet": [
            {
                "CreateTime": "2026-04-24T03:55:48Z",
                "Description": "desc******* ****",
                "Id": "308974*********",
                "Name": "name************"
            }
        ],
        "TotalCount": 1,
        "RequestId": "0997c036-ccac-4730-afa1-09ea8fff667b"
    }
}
```

