**Example 1: 列出命名空间列表**



Input: 

```
tccli scf ListNamespaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Namespaces": [
            {
                "Description": "test",
                "AddTime": "2018-11-27 12:02:25",
                "ModTime": "2018-11-27 12:02:25",
                "Type": "default"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d6b24531-8594-4994-b1a8-f154ec07ff76"
    }
}
```

