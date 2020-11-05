**Example 1: Querying tag keys**



Input: 

```
tccli tag DescribeTagKeys --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 9,
        "Offset": 0,
        "Limit": 15,
        "Tags": [
            "test2",
            "test1",
            "0",
            "string",
            "test",
            "abcbbbb",
            "abcaaaaa",
            "abc",
            "test"
        ],
        "RequestId": "cec4f865-bc87-4858-994e-80771644094d"
    }
}
```

