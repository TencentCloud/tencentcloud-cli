**Example 1: 修改一个CCN的名称和描述**



Input: 

```
tccli vpc ModifyCcnAttribute --cli-unfold-argument  \
    --CcnId ccn-gjug0kul \
    --CcnName new+name \
    --CcnDescription new+description
```

Output: 
```
{
    "Response": {
        "RequestId": "627c2362-890f-4f9e-9158-5e457b80d48b"
    }
}
```

