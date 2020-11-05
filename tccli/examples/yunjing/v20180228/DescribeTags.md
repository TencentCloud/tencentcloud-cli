**Example 1: Getting all server tags**

This example shows you how to get all server tags.

Input: 

```
tccli yunjing DescribeTags --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 2,
                "Name": "Tag name",
                "Count": 123
            }
        ],
        "RequestId": "b12a5e5a-9393-453f-a4d9-b42de0b2bcec"
    }
}
```

