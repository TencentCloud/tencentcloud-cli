**Example 1: 获取导入第三方集群YAML定义**



Input: 

```
tccli tke DescribeExternalClusterSpec --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --IsExtranet False \
    --IsRefreshExpirationTime False
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Spec": "xxxx",
        "Expiration": "2021-09-08T07:04:51Z"
    }
}
```

