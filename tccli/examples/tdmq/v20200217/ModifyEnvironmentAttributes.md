**Example 1: 修改指定命名空间的属性值**

修改指定命名空间的属性值

Input: 

```
tccli tdmq ModifyEnvironmentAttributes --cli-unfold-argument  \
    --EnvironmentId test \
    --MsgTTL 100 \
    --ClusterId pulsar-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "test",
        "NamespaceId": "namespace-5r59xen74x",
        "MsgTTL": 100,
        "Remark": "",
        "RequestId": "7db00a30-933c-4f6f-bba9-79cdf6be7d8c"
    }
}
```

