**Example 1: 调用失败示例**



Input: 

```
tccli bda GetSummaryInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": ""
        },
        "RequestId": "78ec7830-a1c7-42be-bd65-6d0fa25f6fab"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda GetSummaryInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "GroupCount": 10,
        "PersonCount": 100,
        "TraceCount": 1000,
        "RequestId": "9ffccff2-4b52-443f-98f4-eb1f6a30399e"
    }
}
```

