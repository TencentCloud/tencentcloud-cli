**Example 1: 获取所有Web框架数量**



Input: 

```
tccli cwp DescribeAssetWebFrameCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "WebFrames": [
            {
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

