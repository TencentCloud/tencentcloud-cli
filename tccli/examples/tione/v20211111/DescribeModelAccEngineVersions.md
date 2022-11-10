**Example 1: 查询模型加速引擎版本列表**



Input: 

```
tccli tione DescribeModelAccEngineVersions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ModelAccEngineVersions": [
            {
                "EngineVersions": [
                    {
                        "Image": "xx",
                        "Version": "xx"
                    }
                ],
                "ModelFormat": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

