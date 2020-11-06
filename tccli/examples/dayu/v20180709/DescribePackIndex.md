**Example 1: 获取产品总览**



Input: 

```
tccli dayu DescribePackIndex --cli-unfold-argument  \
    --Business bgp
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "TotalPackCount",
                "Value": "0"
            },
            {
                "Key": "AttackPackCount",
                "Value": "0"
            },
            {
                "Key": "BlockPackCount",
                "Value": "0"
            },
            {
                "Key": "ExpiredPackCount",
                "Value": "0"
            },
            {
                "Key": "ExpireingPackCount",
                "Value": "0"
            },
            {
                "Key": "IsolatePackCount",
                "Value": "0"
            }
        ],
        "RequestId": "8f7a9451-2372-4a88-a69d-9868b8991076"
    }
}
```

