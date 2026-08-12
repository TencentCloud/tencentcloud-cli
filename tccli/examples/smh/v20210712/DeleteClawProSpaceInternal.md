**Example 1: 删除空间并放入回收站**



Input: 

```
tccli smh DeleteClawProSpaceInternal --cli-unfold-argument  \
    --LibraryId smh2t6*****76zfg \
    --InstanceId ins-****1943 \
    --ExpectedSpaceId space3******kdg305 \
    --Recoverable True
```

Output: 
```
{
    "Response": {
        "RequestId": "15f9742d-2354-472e-8da3-5207e4cca6e4"
    }
}
```

