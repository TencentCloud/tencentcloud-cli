**Example 1: DescribeContainerEvents**



Input: 

```
tccli tsf DescribeContainerEvents --cli-unfold-argument  \
    --ResourceType instance \
    --ResourceId test-event-6f46bcb6b-sxfcr \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "FirstTimestamp": 0,
                    "LastTimestamp": 0,
                    "Type": "abc",
                    "Kind": "abc",
                    "Name": "abc",
                    "Reason": "abc",
                    "Message": "abc",
                    "Count": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

