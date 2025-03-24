**Example 1: 获取型号和对应版本数量**



Input: 

```
tccli chc DescribeModelVersionList --cli-unfold-argument  \
    --DeviceType server
```

Output: 
```
{
    "Response": {
        "ModelVersionSet": [
            {
                "DevModel": "Test",
                "VersionCount": 1
            }
        ],
        "RequestId": "d8d199be-bde9-4f2b-bcf7-3a979233b66a"
    }
}
```

