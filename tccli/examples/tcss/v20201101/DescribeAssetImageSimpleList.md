**Example 1: 查询镜像简略信息列表**



Input: 

```
tccli tcss DescribeAssetImageSimpleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ImageID": "sha256:27a55a6c3646bdb51f0bedff3a7b87f613c4c69c94b4134c3f7248e1a4bd2ffb",
                "ImageName": "<none>:<none>",
                "ContainerCnt": 0,
                "ScanTime": "2021-01-29T05:26:18.07Z",
                "Size": 12800228
            }
        ],
        "RequestId": "1b4fa00d-257c-4d97-b175-cd78c7a8a362",
        "TotalCount": 339
    }
}
```

