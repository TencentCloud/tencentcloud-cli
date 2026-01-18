**Example 1: 跨地域同步自定义镜像**

向两个地域同步自定义镜像。

Input: 

```
tccli lighthouse SyncBlueprint --cli-unfold-argument  \
    --BlueprintId lhbp-ls883feh \
    --DestinationRegions ap-singapore ap-hongkong
```

Output: 
```
{
    "Response": {
        "DestinationRegionBlueprintSet": [
            {
                "Region": "ap-singapore",
                "BlueprintId": "lhbp-lf3gjs2f"
            },
            {
                "Region": "ap-hongkong",
                "BlueprintId": "lhbp-lfle246l"
            }
        ],
        "RequestId": "e35a5b7b-4dfa-49f8-8729-ba5c504807e0"
    }
}
```

