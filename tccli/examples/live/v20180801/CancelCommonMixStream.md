**Example 1: 取消示例**

根据session id取消混流。

Input: 

```
tccli live CancelCommonMixStream --cli-unfold-argument  \
    --MixStreamSessionId test_room
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

