**Example 1: DescribeEmployees1**

DescribeEmployees1

Input: 

```
tccli eportrait DescribeEmployees --cli-unfold-argument  \
    --Eid 4e8eb65c5f996b50e9b8e93be211a483 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "JobTitle": "董事",
                "Name": "Charles St leger Searle"
            },
            {
                "JobTitle": "监事",
                "Name": "周昭钦"
            },
            {
                "JobTitle": "董事长兼总经理",
                "Name": "奚丹"
            },
            {
                "JobTitle": "董事",
                "Name": "马化腾"
            }
        ],
        "RequestId": "9574845b-1eae-4c76-8940-80ee861247a2",
        "TotalCount": 4
    }
}
```

