**Example 1: 退款资源包**

退款资源包


Input: 

```
tccli cynosdb RefundResourcePackage --cli-unfold-argument  \
    --PackageId abc
```

Output: 
```
{
    "Response": {
        "DealNames": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

