**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveSnapshotTemplate --cli-unfold-argument  \
    --TemplateId 1000
```

Output: 
```
{
    "Response": {
        "Template": {
            "TemplateId": 1000,
            "TemplateName": "testName",
            "Description": "active_template",
            "SnapshotInterval": 10,
            "Width": 250,
            "Height": 250,
            "PornFlag": 0,
            "CosAppId": 934258,
            "CosBucket": "bucket",
            "CosRegion": "beijing",
            "CosPrefix": "live",
            "CosFileName": "myfilename"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

