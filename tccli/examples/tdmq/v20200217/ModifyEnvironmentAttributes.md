**Example 1: 修改指定命名空间的属性值**

修改指定命名空间的属性值

Input: 

```
tccli tdmq ModifyEnvironmentAttributes --cli-unfold-argument  \
    --EnvironmentId devNs \
    --MsgTTL 100 \
    --ClusterId pulsar-5r59xd4vnx
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "devNs",
        "NamespaceId": "namespace-5r59xen74x",
        "MsgTTL": 100,
        "Remark": "devRemark",
        "RequestId": "7db00a30-933c-4f6f-bba9-79cdf6be7d8c"
    }
}
```

