**Example 1: Sample request**



Input: 

```
tccli live DescribeLiveWatermarkRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "CreateTime": "2018-09-12T15:52:01Z",
                "UpdateTime": "2018-10-12T18:00:05Z",
                "TemplateID": 1000,
                "DomainName": "yourdomain.test.com",
                "AppName": "live",
                "StreamName": "stream1"
            }
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

