**Example 1: Deleting a Forwarding Rule of a Layer-7 Listener**

Delete a forwarding rule of a layer-7 listener.

Input: 

```
tccli gaap DeleteRule --cli-unfold-argument  \
    --ListenerId 0\
    --RuleId rule-18vhg67\
    --Force 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

