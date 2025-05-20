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
        "RequestId": "647f2a53-c672-45fa-980b-385423898a69"
    }
}
```

