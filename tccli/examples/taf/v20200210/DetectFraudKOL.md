**Example 1: DetectFraudKOL**



Input: 

```
tccli taf DetectFraudKOL --cli-unfold-argument  \
    --BspData.DataList.0.Type 1 \
    --BspData.DataList.0.Id dgxyx0769 \
    --BspData.DataList.0.Name testname \
    --BspData.DataList.0.Phone 15718322162 \
    --BspData.DataList.0.AgentInfo kol_agent
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": [
                {
                    "Id": "dgxyx0769",
                    "IsCheck": 1,
                    "FraudPScore": 23,
                    "EvilPScore": 56
                }
            ]
        },
        "RequestId": "19f4cd87-29b3-4fac-bf36-62cd7e785e27"
    }
}
```

