**Example 1: 弱口令配置**



Input: 

```
tccli cwp DescribeBaselineWeakPasswordList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PasswordId": 2431,
                "WeakPassword": "132",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2432,
                "WeakPassword": "133",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2433,
                "WeakPassword": "134",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2434,
                "WeakPassword": "135",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2435,
                "WeakPassword": "136",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2436,
                "WeakPassword": "137",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2437,
                "WeakPassword": "138",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2438,
                "WeakPassword": "139",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2439,
                "WeakPassword": "140",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            },
            {
                "PasswordId": 2440,
                "WeakPassword": "141",
                "CreateTime": "2022-07-28 21:37:22",
                "ModifyTime": "2022-07-28 21:37:22"
            }
        ],
        "RequestId": "a5ac3a8f-b4a5-4d0c-a8ef-c24601bffd98",
        "Total": 998
    }
}
```

