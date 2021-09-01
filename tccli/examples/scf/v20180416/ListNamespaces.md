**Example 1: 列出命名空间列表**



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
        "TotalCount": 1,
        "RequestId": "xx",
        "Namespaces": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Type": "xx",
                "Description": "xx",
                "Name": "xx"
            }
        ]
    }
}
```

