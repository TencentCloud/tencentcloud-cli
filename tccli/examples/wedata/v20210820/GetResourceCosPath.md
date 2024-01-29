**Example 1: 资源管理-获取 cos 可用列表**

获取 cos 可用列表

Input: 

```
tccli wedata GetResourceCosPath --cli-unfold-argument  \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

