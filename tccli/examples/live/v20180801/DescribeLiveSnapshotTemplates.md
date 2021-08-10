**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveSnapshotTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": 1000,
                "TemplateName": "testName",
                "Description": "test",
                "SnapshotInterval": 10,
                "Width": 250,
                "Height": 250,
                "PornFlag": 0,
                "CosAppId": 123,
                "CosBucket": "bucket",
                "CosRegion": "beijing",
                "CosPrefix": "xx",
                "CosFileName": "xx"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

