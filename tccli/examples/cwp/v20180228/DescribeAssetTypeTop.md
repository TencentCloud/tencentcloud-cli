**Example 1: 获取各种类型资源Top5**



Input: 

```
tccli cwp DescribeAssetTypeTop --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Database": [
            {
                "Key": "SQL Server",
                "Value": 2,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "Port": [
            {
                "Key": "10250",
                "Value": 21,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "Process": [
            {
                "Key": "svchost.exe",
                "Value": 241,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "RequestId": "1693599e-ff8f-4a8c-ae39-b4d9ba3ae9bf",
        "Software": [
            {
                "Key": "NTP",
                "Value": 37,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "User": [
            {
                "Key": "lp",
                "Value": 53,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "WebApp": [
            {
                "Key": "phpMyAdmin",
                "Value": 6,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "WebFrame": [
            {
                "Key": "hibernate",
                "Value": 3,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "WebLocation": [
            {
                "Key": "localhost",
                "Value": 9,
                "NewCount": 0,
                "Desc": "none"
            }
        ],
        "WebService": [
            {
                "Key": "Nginx",
                "Value": 25,
                "NewCount": 0,
                "Desc": "none"
            }
        ]
    }
}
```

