**Example 1: 验证域名是否存在**

验证域名是否存在

Input: 

```
tccli waf DescribeHostLimit --cli-unfold-argument  \
    --Domain randy.qcloudwaf.com \
    --InstanceID waf_2kxtpov60i9y7i05 \
    --AlbType clb
```

Output: 
```
{
    "Response": {
        "RequestId": "97720395-7456-4a21-bcd9-1f32a7deaa90",
        "Error": {
            "Code": "ResourceInUse",
            "Message": "DomainExisted"
        }
    }
}
```

