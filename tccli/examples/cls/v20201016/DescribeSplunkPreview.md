**Example 1: Splunk日志投递预览**



Input: 

```
tccli cls DescribeSplunkPreview --cli-unfold-argument  \
    --TopicId d1d7d473-827e-4dad-9a42-f0287ad43125 \
    --MetadataInfo.Format json \
    --MetadataInfo.MetaFields __TIMESTAMP__
```

Output: 
```
{
    "Response": {
        "PreviewInfos": [],
        "RequestId": "0c600166-11d3-46dd-b43f-09e1bb043125"
    }
}
```

