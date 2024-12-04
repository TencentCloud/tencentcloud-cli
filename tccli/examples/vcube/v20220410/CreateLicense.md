**Example 1: 绑定license**

在已有应用下新增license


Input: 

```
tccli vcube CreateLicense --cli-unfold-argument  \
    --ApplicationId abc \
    --ResourceIds abc \
    --Group 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

