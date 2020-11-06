**Example 1: Querying resource tags**



Input: 

```
tccli tag DescribeResourceTagsByResourceIds --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourcePrefix instance \
    --ResourceRegion ap-beijing \
    --ResourceIds ins-1234
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Offset": 0,
        "Limit": 15,
        "Tags": [
            {
                "TagKey": "string",
                "TagValue": "string",
                "TagKeyMd5": "cc4dd1da7e1a754534215f02fb9ba85d",
                "TagValueMd5": "cc4dd1da7e1a754534215f02fb9ba85d",
                "ResourceId": "ins-1234"
            }
        ],
        "RequestId": "34bdd6cc-34b0-4ef4-9051-be9a5294be8e"
    }
}
```

