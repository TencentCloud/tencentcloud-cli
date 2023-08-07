**Example 1: 用户下无添加计划通道**

 

Input: 

```
tccli iss ListRecordPlanChannels --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "List": null
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

**Example 2: 用户下有添加计划通道**

 

Input: 

```
tccli iss ListRecordPlanChannels --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                "0001a415-b9c1-****-****-b13cfb96c778",
                "0003a068-c8c1-****-****-6e1d46b1e1f3",
                "000fb77b-6b25-****-****-d4aff5503d70",
                "0020a697-606d-****-****-c836d9f95075"
            ]
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

