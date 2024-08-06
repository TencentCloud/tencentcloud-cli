**Example 1: 正常请求示例**



Input: 

```
tccli advisor DescribeResourceBelong --cli-unfold-argument  \
    --ProductId Auto Scaling \
    --RegionId ap-guangzhou \
    --ResourceIds test-resource-id \
    --PluginKey 3b554194-0641-4d1b-ahsdqwkdhj-wsdwsd \
    --Conditions.0.Key ClusterId \
    --Conditions.0.Value cls-nt48x5zs
```

Output: 
```
{
    "Response": {
        "BelongResourceIds": [
            "test-resource-id-1"
        ],
        "NotBelongResourceIds": [
            "abc"
        ],
        "RequestId": "4b8d2f80-755a-4beb-9d26-232306c0a9b1"
    }
}
```

