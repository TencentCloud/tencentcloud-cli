**Example 1: 删除字段值替换规则**



Input: 

```
tccli rum DeleteTDEMFieldTransformRule --cli-unfold-argument  \
    --Id 31 \
    --AppId 11
```

Output: 
```
{
    "Response": {
        "Deleted": true,
        "Id": 31,
        "Message": "rule deleted successfully",
        "RequestId": "b8a13563-3114-45bd-a7b8-980b880aea5e"
    }
}
```

