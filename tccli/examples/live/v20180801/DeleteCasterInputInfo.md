**Example 1: 请求示例**

删除导播台63501的输入源1。

Input: 

```
tccli live DeleteCasterInputInfo --cli-unfold-argument  \
    --InputIndex 1 \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

