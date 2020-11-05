**Example 1: Getting security event message**

This example shows you how to get the security event message data.

Input: 

```
tccli yunjing DescribeSecurityDynamics --cli-unfold-argument  \
    --Limit 10\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityDynamics": [
            {
                "Uuid": "add4a78a-0d59-11e8-b7ab-00e081e1a5c5",
                "EventTime": "2018-10-08 12:12:22",
                "EventType": "MALWARE",
                "Message": "5 malicious files found on host 10.10.10.12"
            }
        ],
        "TotalCount": 100
    }
}
```

