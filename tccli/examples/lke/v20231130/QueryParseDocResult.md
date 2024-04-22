**Example 1: 查询文档解析结果**

查询文档解析结果

Input: 

```
tccli lke QueryParseDocResult --cli-unfold-argument  \
    --TaskId D78iBBGi
```

Output: 
```
{
    "Response": {
        "Name": "D78iBBGi.zip",
        "Reason": "",
        "RequestId": "acd2b5f3-350f-4171-92be-e1c70f3e73d7",
        "Status": "success",
        "Url": "https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/%2Fatomic/2/D78iBBGi.zip?q-sign-algorithm=sha1&q-ak=xxxxxxxxx&q-sign-time=1706792626%3B1706796226&q-key-time=1706792626%3B1706796226&q-header-list=host&q-url-param-list=&q-signature=e3d46a97846b256ff89f3698*******************",
        "Usage": {
            "TotalPages": 1
        }
    }
}
```

