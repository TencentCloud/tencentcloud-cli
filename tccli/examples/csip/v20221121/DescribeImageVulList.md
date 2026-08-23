**Example 1: 查询镜像漏洞列表**



Input: 

```
tccli csip DescribeImageVulList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "ImageVulList": [
            {
                "ID": 22624,
                "ImageId": "681",
                "OwnerAccountName": "700002365149",
                "OwnerAppId": 260083796,
                "OwnerUin": "700002365149"
            }
        ],
        "TotalCount": 7,
        "RequestId": "b88efe8e-0ea8-4017-807d-9a34544db703"
    }
}
```

