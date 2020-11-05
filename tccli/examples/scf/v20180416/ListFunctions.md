**Example 1: Querying Functions Based on Tags**

It queries functions whose status tag is `dev` and owner tag is `me`.

Input: 

```
tccli scf ListFunctions --cli-unfold-argument  \
    --Filters.0.Name tag-status\
    --Filters.0.Values dev\
    --Filters.1.Name tag-owner\
    --Filters.1.Values me
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "FunctionId": "lam-xxxxxxx",
                "Namespace": "default",
                "FunctionName": "test",
                "ModTime": "2018-04-08 19:02:20",
                "AddTime": "2018-04-08 15:18:49",
                "Runtime": "Python2.7"
            }
        ],
        "TotalCount": 1,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: Obtaining a Function List**

It queries functions whose status tag is dev and owner tag is me.

Input: 

```
tccli scf ListFunctions --cli-unfold-argument  \
    --Limit 2\
    --Order ASC
```

Output: 
```
{
    "Response": {
        "Functions": [
            {
                "FunctionId": "lam-xxxxxxx",
                "Namespace": "default",
                "FunctionName": "test",
                "ModTime": "2018-04-08 19:02:20",
                "AddTime": "2018-04-08 15:18:49",
                "Runtime": "Python2.7"
            }
        ],
        "TotalCount": 1,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

