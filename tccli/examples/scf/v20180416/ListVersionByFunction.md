**Example 1: 查询函数版本**



Input: 

```
tccli scf ListVersionByFunction --cli-unfold-argument  \
    --FunctionName xxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "FunctionVersion": [
            "$LATEST",
            "3",
            "2",
            "1"
        ],
        "RequestId": "xx",
        "Versions": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Version": "xx",
                "Description": "xx",
                "Status": "xx"
            },
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Version": "xx",
                "Description": "xx",
                "Status": "xx"
            },
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Version": "xx",
                "Description": "xx",
                "Status": "xx"
            },
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Version": "xx",
                "Description": "xx",
                "Status": "xx"
            }
        ]
    }
}
```

