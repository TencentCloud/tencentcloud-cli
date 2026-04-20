**Example 1: 更新索引**



Input: 

```
tccli es UpdateIndex --cli-unfold-argument  \
    --InstanceId es-h3pzdpd6 \
    --IndexName asd \
    --IndexType normal \
    --UpdateMetaJson {"mappings":{"properties":{"aa":{"analyzer":"standard","index":true,"type":"text"}}},"settings":{}}
```

Output: 
```
{
    "Response": {
        "RequestId": "6cf36e17-abdf-4a75-a95a-78a0e59fc959"
    }
}
```

