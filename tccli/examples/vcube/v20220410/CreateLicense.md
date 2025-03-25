**Example 1: 绑定license**

在已有应用下新增license


Input: 

```
tccli vcube CreateLicense --cli-unfold-argument  \
    --ApplicationId 837245 \
    --ResourceIds xmc534db52193ab436e89 \
    --Group 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

