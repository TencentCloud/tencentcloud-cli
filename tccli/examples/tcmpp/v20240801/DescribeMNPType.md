**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPType --cli-unfold-argument  \
    --PlatformId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeName": "abc",
                "TypeValue": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

