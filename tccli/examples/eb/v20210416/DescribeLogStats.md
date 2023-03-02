**Example 1: demo1**

查询每分钟统计值，不以status分组

Input: 

```
tccli eb DescribeLogStats --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "Status": "all",
                "Data": [
                    {
                        "Count": 0,
                        "Timestamp": 0
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: demo2**

查询每分钟统计值，以status分组

Input: 

```
tccli eb DescribeLogStats --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "Status": "0",
                "Data": [
                    {
                        "Count": 18,
                        "Timestamp": 1675656420000
                    },
                    {
                        "Timestamp": 1675656480000
                    }
                ]
            },
            {
                "Status": "1",
                "Data": [
                    {
                        "Count": 18,
                        "Timestamp": 1675656420000
                    },
                    {
                        "Timestamp": 1675656480000
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

