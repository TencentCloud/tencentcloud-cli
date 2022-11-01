**Example 1: 查询服务的历史版本**



Input: 

```
tccli tione DescribeModelServiceHistory --cli-unfold-argument  \
    --ServiceId xxxxxx
```

Output: 
```
{
    "Response": {
        "ServiceHistory": [
            {
                "Revision": "1",
                "UpdateTime": "2022-01-15T17:32:52+08:00",
                "Image": "nignx",
                "ModelFile": "",
                "RawData": "xxxxxxxxxxxx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "bc2997e4-cceb-4a75-8bdb-95574cf50301"
    }
}
```

