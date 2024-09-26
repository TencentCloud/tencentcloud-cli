**Example 1: DescribeVerifyReport**

验签报告查询

Input: 

```
tccli ca DescribeVerifyReport --cli-unfold-argument  \
    --SignatureId 692175715651854336
```

Output: 
```
{
    "Response": {
        "ReportUrl": "https://file.nmgsca.com/verified/%E6%B5%8B%E8%AF%95PDF-%E7%94%B5%E5%AD%90%E9%AA%8C%E7%AD%BE%E6%8A%A5%E5%91%8A-1795026427158528.pdf?q-sign-algorithm=sha1&q-ak=AKIDypWzDKL9IKFxY3SxMet5AGJTf3JMKGzW&q-sign-time=1727259339%3B1727302539&q-key-time=1727259339%3B1727302539&q-header-list=host&q-url-param-list=&q-signature=63f6173318070deb130976c8ea4185ca9e66ba7b",
        "RequestId": "292ea5cb-4e80-417c-92fd-02d869545682"
    }
}
```

