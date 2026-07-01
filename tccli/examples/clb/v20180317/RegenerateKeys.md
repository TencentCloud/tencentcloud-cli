**Example 1: 重新生成Key**



Input: 

```
tccli clb RegenerateKeys --cli-unfold-argument  \
    --ModelRouterId cmr-jcxor1gp \
    --KeyIds vkey-g2kyvhih
```

Output: 
```
{
    "Response": {
        "RegeneratedKeys": [
            {
                "Key": "sk-HvvyVk2DvoMuG1t0MEzz4qLqWZ8-xNUlVzUZo1jtzW3opZ9eMok0nfgEhd-lLFgqKxY3d-0qFy2aohD5sKRPJu1Hlv1irSX6-nStS-9xXA",
                "KeyId": "vkey-g2kyvhih"
            }
        ],
        "RequestId": "e6ca32ca-5157-4feb-9692-4a3d8962df53"
    }
}
```

