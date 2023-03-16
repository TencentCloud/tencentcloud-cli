**Example 1: 列出命名空间列表**

列出命名空间列表

Input: 

```
tccli scf ListNamespaces --cli-unfold-argument  \
    --SearchKey.0.Key Namespace \
    --SearchKey.0.Value dev
```

Output: 
```
{
    "Response": {
        "Namespaces": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Description": "abc",
                "Name": "abc",
                "Type": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

