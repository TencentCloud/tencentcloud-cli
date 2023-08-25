**Example 1: 退款资源包**

退款资源包


Input: 

```
tccli cynosdb RefundResourcePackage --cli-unfold-argument  \
    --PackageId package-abcd1234
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

