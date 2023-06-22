**Example 1: 创建音画质检测模板。**

创建音画质检测模板。

Input: 

```
tccli vod CreateQualityInspectTemplate --cli-unfold-argument  \
    --SubAppId 123 \
    --Name test \
    --Comment abc \
    --JitterConfigure.Switch ON
```

Output: 
```
{
    "Response": {
        "Definition": 20001,
        "RequestId": "3c140219-cfe9-470e-b241-907873d6fb03"
    }
}
```

