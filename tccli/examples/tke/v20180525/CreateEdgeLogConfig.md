**Example 1: 创建日志采集规则**

创建边缘集群日志采集规则

Input: 

```
tccli tke CreateEdgeLogConfig --cli-unfold-argument  \
    --LogConfig '{"apiVersion":"cls.cloud.tencent.com/v1","kind":"LogConfig"... }' \
    --ClusterId cls-1234abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

