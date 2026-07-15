**Example 1: 查询所有可用区**

查询所有可用区

Input: 

```
tccli alb DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Zones": [
            {
                "ZoneId": "ap-guangzhou-2",
                "LocalName": "广州二区",
                "ZoneStatus": "available"
            },
            {
                "ZoneId": "ap-guangzhou-3",
                "LocalName": "广州三区",
                "ZoneStatus": "available"
            }
        ],
        "RequestId": "4e5df572-e085-4e30-a3bb-d520768d1473"
    }
}
```

