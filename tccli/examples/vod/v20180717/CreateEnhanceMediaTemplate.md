**Example 1: 创建音画质重生模板。**

创建音画质重生模板。

Input: 

```
tccli vod CreateEnhanceMediaTemplate --cli-unfold-argument  \
    --SubAppId 123 \
    --Name test \
    --Comment abc \
    --RebuildVideoInfo.RepairInfo.Switch ON \
    --Container mp4
```

Output: 
```
{
    "Response": {
        "Definition": 20001,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

