**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeSimpleTeamList --cli-unfold-argument  \
    --PlatformId abc \
    --TeamRoleTypeList 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "DataList": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

