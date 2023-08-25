**Example 1: 示例**



Input: 

```
tccli dsgc DeleteDSPAMetaResource --cli-unfold-argument  \
    --DspaId dspa-6fb60936 \
    --ResourceIDs ins-xd48jxyk-8587a43d
```

Output: 
```
{
    "Response": {
        "RequestId": "f767c836-43b4-4165-b48e-76c4dea71325",
        "DspaId": "dspa-6fb60936",
        "Results": [
            {
                "Result": "success",
                "ResultDescription": "resource delete success",
                "ResourceId": "ins-xd48jxyk-8587a43d",
                "MetaType": "mysql_like_proto"
            }
        ]
    }
}
```

