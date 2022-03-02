**Example 1: 转换集群付费模式**



Input: 

```
tccli tdcpg TransformClusterPayMode --cli-unfold-argument  \
    --ClusterId tdcpg-xxx \
    --Period 1 \
    --CurrentPayMode POSTPAID_BY_HOUR \
    --TargetPayMode PREPAID
```

Output: 
```
{
    "Response": {
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

