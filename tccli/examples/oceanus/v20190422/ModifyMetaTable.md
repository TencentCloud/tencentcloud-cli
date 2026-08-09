**Example 1: 元数据表编辑**



Input: 

```
tccli oceanus ModifyMetaTable --cli-unfold-argument  \
    --ClusterId cluster-xxx \
    --TableId 1 \
    --SqlCode Q1JFQVRFIFRBQkxFIGRhdGFnZW5fc291cmNlX3RhYmxlICggCiAgICBpZCBJTlQsIAogICAgbmFtZSBTVFJJTkcgCikgV0lUSCAoCidjb25uZWN0b3InPSdkYXRhZ2VuJywKJ3Jvd3MtcGVyLXNlY29uZCcgPSAnMScKKTs= \
    --FlinkVersion Flink-1.13 \
    --WorkSpaceId space-xx \
    --Remark remark
```

Output: 
```
{
    "Response": {
        "RequestId": "407D2293-E7A8-456B-97F8-B242677AE71D"
    }
}
```

