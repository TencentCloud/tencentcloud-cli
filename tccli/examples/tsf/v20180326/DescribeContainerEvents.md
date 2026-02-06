**Example 1: DescribeContainerEvents**



Input: 

```
tccli tsf DescribeContainerEvents --cli-unfold-argument  \
    --ResourceType instance \
    --ResourceId test-event-6f46bcb6b-sxfcr \
    --GroupId group-9yn2q8yd \
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
                    "Type": "instance",
                    "Kind": "SERVER",
                    "Name": "test-event",
                    "Reason": "this is a reason",
                    "Message": "this is a msg",
                    "Count": 0
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

