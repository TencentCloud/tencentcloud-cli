**Example 1: 查询可加速域名**

查询可加速域名

Input: 

```
tccli vpc DescribeOverseaAcceleratorDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccelerateDomain": [
            {
                "Domain": "buy.itunes.apple.com",
                "DomainShort": "APPLEPAY"
            }
        ],
        "RequestId": "e4de1feb-adaf-4cfd-ad3c-db9aecfe549d"
    }
}
```

