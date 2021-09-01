**Example 1: 示例**



Input: 

```
tccli cwp DescribeWebPageProtectStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FileTamperNum": [
            {
                "Name": "/tmp",
                "Num": 56
            },
            {
                "Name": "/data",
                "Num": 1
            },
            {
                "Name": "/var",
                "Num": 6
            },
            {
                "Name": "/root",
                "Num": 4
            },
            {
                "Name": "/dev",
                "Num": 33
            }
        ],
        "ProtectFileType": [
            {
                "Name": "boot",
                "Num": 1
            },
            {
                "Name": "start",
                "Num": 2
            },
            {
                "Name": "stop",
                "Num": 3
            },
            {
                "Name": "php",
                "Num": 10
            }
        ],
        "RequestId": "36c8cea5-7be7-4b61-8212-1ceb63330a5c"
    }
}
```

