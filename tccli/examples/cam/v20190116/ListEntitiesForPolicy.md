**Example 1: Querying the list of entities associated with a policy**



Input: 

```
tccli cam ListEntitiesForPolicy --cli-unfold-argument  \
    --PolicyId 524497\
    --Page 1\
    --Rp 10\
    --EntityFilter All
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": "1133398",
                "RelatedType": 1,
                "Uin": 3449203261,
                "Name": "test1"
            }
        ],
        "TotalNum": 1,
        "RequestId": "836d7034-9854-44f0-9d4a-ee57842f8644"
    }
}
```

