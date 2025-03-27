**Example 1: 创建音画质重生模板。**

创建音画质重生模板。

Input: 

```
tccli vod CreateEnhanceMediaTemplate --cli-unfold-argument  \
    --SubAppId 12511111104 \
    --Name template1 \
    --Comment this is a template \
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

